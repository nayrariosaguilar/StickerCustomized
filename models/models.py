from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'stickers.material'
    _description = 'Materiales para fabricación de stickers'

    product_template_id = fields.Many2one(
        'product.template',
        string="Material",
        required=True,
        ondelete='cascade'
    )

    # Solo dos categorías: Material Base o Tinta
    categoria_material = fields.Selection(
        [('material_base', 'Material Base'), ('tinta', 'Tinta')],
        string="Categoría del Material",
        required=True
    )

    proveedor_principal_id = fields.Many2one('res.partner', string="Proveedor principal")
    costo_por_unidad = fields.Float(string="Costo por unidad", help="Costo unitario del material")
    especificaciones_tecnicas = fields.Text(string="Especificaciones técnicas")
    fecha_ultima_compra = fields.Date(string="Fecha de última compra")

    # Cantidad disponible en stock (obtenida de product.template)

    cantidad_disponible = fields.Float(
        string="Cantidad disponible (m²)",
        compute="_compute_cantidad_disponible",
        store=True
    )
    image_1920 = fields.Image(
        string="Imagen del material",
        related="product_template_id.image_1920",
        readonly=False  # Permitir cambiar la imagen desde aquí
    )

    @api.depends('product_template_id.qty_available')
    def _compute_cantidad_disponible(self):
        """Obtiene la cantidad disponible del stock de Odoo"""
        for material in self:
            material.cantidad_disponible = material.product_template_id.qty_available

    @api.depends('cantidad_disponible')
    def _compute_cantidad_m2(self):
        """La cantidad en m² ahora es igual a la cantidad disponible"""
        for material in self:
            material.cantidad_en_m2 = material.cantidad_disponible

    def consumir_material(self, cantidad_m2):
        """
        Resta material en m² al stock disponible.
        Se usa en el modelo Sticker para descontar el material base.
        """
        for material in self:
            if material.categoria_material == 'tinta':
                raise ValidationError("No se puede descontar tinta del stock directamente.")

            if material.cantidad_en_m2 < cantidad_m2:
                raise ValidationError(f"No hay suficiente stock de {material.nombre} en m².")

            material.product_template_id.qty_available -= cantidad_m2  # Restar del stock real en Odoo

class StickersCustomized(models.Model):
    _name = 'stickers.customized'
    _description = "Details of customized stickers"

    id_material = fields.Many2many(
        'stickers.material',
        string="Materials",
        help="Materials used for the sticker"
    )
    id_product = fields.Many2one(
        'product.product',
        string="Product",
        help="Product associated with the sticker"
    )
    width = fields.Integer(
        string="Width",
        required=True,
        help="Width of the sticker"
    )
    height = fields.Integer(
        string="Height",
        required=True,
        help="Height of the sticker"
    )

    image_personalized = fields.Image(
        string="Image",
        help="Upload an image for your sticker"
    )

    id_color = fields.Many2many(
        'stickers.color',
        string="Colors",
        help="Colors used for the sticker"
    )
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

