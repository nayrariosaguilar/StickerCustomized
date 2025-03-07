from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StickersScale(models.Model):
    _name = 'stickers.scale'
    _description = "Scales available for stickers"

    name = fields.Char(
        string="Scale Name",
        size=11,
        required=True,
        help="Name of the scale",
        default="cm"
    )

class StickersShape(models.Model):
    _name = 'stickers.shape'
    _description = "Shapes available for stickers"
    name = fields.Char(
        string="Shape",
        size=20,
        required=True,
        help="Name of the shape"
    )
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The shape name must be unique!')
    ]

class StickersPrinting(models.Model):
    _name = 'stickers.printing'
    _description = "Printing types available for stickers"
    name = fields.Char(
        string="Printing Type",
        size=30,
        required=True,
        help="Name of the printing type"
    )

class StickersMaterial(models.Model):
    _name = 'stickers.material'
    _description = 'Materiales para fabricación de stickers'

    product_template_id = fields.Many2one(
        'product.template',
        string="Material",
        required=True,
        ondelete='cascade'
    )
    main_supplier_id = fields.Many2one('res.partner', string="Proveedor principal")
    cost_unit = fields.Float(string="Costo por unidad", help="Costo unitario del material")
    last_purchase_date = fields.Date(string="Fecha de última compra")
    stock = fields.Float(
        string="Cantidad disponible",
        compute="_compute_stock",
        store=True
    )
    image_1920 = fields.Image(
        string="Imagen del material",
        related="product_template_id.image_1920",
        readonly=False
    )

    @api.depends('product_template_id.virtual_available')
    def _compute_stock(self):
        for material in self:
            material.stock = material.product_template_id.virtual_available

class StickersCustomized(models.Model):
    _name = 'stickers.customized'
    _description = "Details of customized stickers"

    name = fields.Char(
        string="Sticker Name",
        required=True,
        help="Name of the sticker"
    )
    #La id del tipo de impresión del sticker, solo puede ser 1
    id_finish = fields.Many2one(
        'stickers.printing',
        string="Printing Type",
        help="Type of printing for the sticker"
    )
    #La id de la escala del sticker, solo puede ser 1
    id_scale = fields.Many2one(
        'stickers.scale',
        string="Scale",
        help="Scale of the sticker"
    )
    #La id de la forma del sticker, solo puede ser 1
    id_shape = fields.Many2one(
        'stickers.shape',
        string="Shape",
        help="Shape of the sticker"
    )
    #La id del producto que se va a crear a partir de los datos del sticker
    id_product = fields.Many2one(
        'product.product',
        string="Product",
        help="Product associated with the sticker"
    )
    #La id del material que se va a utilizar para el sticker, puede ser más de uno
    id_material = fields.Many2many(
        'stickers.material',
        string="Materials",
        help="Materials used for the sticker"
    )
    #La anchura del sticker (puede ser en cm, mm, pulgadas, etc)
    width = fields.Integer(
        string="Width",
        required=True,
        help="Width of the sticker"
    )
    #La altura del sticker (puede ser en cm, mm, pulgadas, etc)
    height = fields.Integer(
        string="Height",
        required=True,
        help="Height of the sticker"
    )
    #Añadimos un campo para que el usuario puede poner una foto del diseño de los stickers
    image_personalized = fields.Image(
        string="Image",
        help="Upload an image for your sticker"
    )
    #Herencia de los colores disponibles en productos (desde product.attribute.value podemos acceder a los colores y añadir más)
    id_color = fields.Many2many(
        'product.attribute.value',
        string="Color",
        domain="[('attribute_id.display_type', '=', 'color')]",
        help="Select a color for the sticker"
    )

#El api.model se encargará de crear un nuevo producto a partir de la clase stickerCustomized (en products.products)

    @api.model
    def create(self, vals):
         # Crea una instancia de sticker
        sticker = super(StickersCustomized, self).create(vals)
        # A partir de esta instancia se recoge el nombre el id y el precio "si lo tuvieramos"
        product = self.env['product.product'].create({
             'name': f": {sticker.name}",
             'type': 'consu',
             'list_price': 0,
             'default_code': f"Sticker-{sticker.id}",
         })
        #Se relaciona el producto con el sticker
        sticker.id_product = product.id
        return sticker
#Le hemos añadidos la restricción de que la altura y la anchura no puede ser negativa
    @api.constrains('width')
    def _check_width_positive(self):
        for record in self:
            if record.width <= 0:
                raise ValidationError('The width must be greater than zero!')

    @api.constrains('height')
    def _check_height_positive(self):
        for record in self:
            if record.height <= 0:
                raise ValidationError('The height must be greater than zero!')
#Nuestro onchange se encarga de advertir al usuario de que el stock del material que ha selecciona es bajo (menos de 10 unidades)
    @api.onchange('id_material')
    def onchange_material(self):
        if self.id_material:
            for material in self.id_material:
                if material.stock < 10:
                    return {
                        'warning': {
                            'title': 'Stock Bajo',
                            'message': f'El material {material.product_template_id.name} tiene pocas existencias ({material.stock})'
                        }
                    }