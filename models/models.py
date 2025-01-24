from odoo import models, fields, api

class StickersMaterial(models.Model):
    _name = 'stickers.material'
    _description = "Materials for stickers"
    name = fields.Char(
        string="Material Name",
        size=50,
        required=True,
        help="Name of the material"
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

def name_get(self):
    result = []
    for record in self:
        # Combina el id y el nombre, o solo el nombre
        result.append((record.id, record.name))
    return result

class StickersColor(models.Model):
    _name = 'stickers.color'
    _description = "Colors available for stickers"

    color_name = fields.Char(
        string="Color Name",
        size=100,
        required=True,
        help="Name of the color",
        default="Blanco"
    )
    category = fields.Selection(
        [
            ('1', 'Rojos y Rosas'),
            ('2', 'Naranjas'),
            ('3', 'Amarillos'),
            ('4', 'Verdes'),
            ('5', 'Azules'),
            ('6', 'Morados y Violetas'),
            ('7', 'Marrones'),
            ('8', 'Grises y Neutros'),
            ('9', 'Negros'),
            ('10', 'Blancos'),
        ],
        string="Color Category",
        required=True,
        help="Category to which this color belongs"
    )
_sql_constraints = [
    ('unique_material_name', 'UNIQUE(color_name)', 'The color name must be unique'),
]


class StickersScale(models.Model):
    _name = 'stickers.scale'
    _description = "Scales available for stickers"
    name = fields.Char(
        string="Scale Name",
        size=11,
        required=True,
        help="Name of the scale"
    )

    def name_get(self):
        """Generic name_get method for models with a 'name' field."""
        result = []
        for record in self:
            result.append((record.id, record.name))
        return result


class StickersPrinting(models.Model):
    _name = 'stickers.printing'
    _description = "Printing types available for stickers"
    name = fields.Char(
        string="Scale Name",
        size=30,
        required=True,
        help="Name of the scale"
    )

    def name_get(self):
        """Generic name_get method for models with a 'name' field."""
        result = []
        for record in self:
            result.append((record.id, record.name))
        return result


class StickersCustomized(models.Model):
    _name = 'stickers.customized'
    _description = "Details of customized stickers"

    id_finish = fields.Many2one(
        'stickers.printing',
        string="Printing Type",
        help="Type of printing for the sticker"
    )
    id_scale = fields.Many2one(
        'stickers.scale',
        string="Scale",
        help="Scale of the sticker"
    )
    id_shape = fields.Many2one(
        'stickers.shape',
        string="Shape",
        help="Shape of the sticker"
    )
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
    message_personalized = fields.Text(
        string="Personalized Message",
        help="Custom message for the sticker"
    )
    image_personalized = fields.Image(
        string="Image",
        help="Upload an image for your sticker"
    )
    category_filter_color = fields.Selection(
        [
            ('1', 'Rojos y Rosas'),
            ('2', 'Naranjas'),
            ('3', 'Amarillos'),
            ('4', 'Verdes'),
            ('5', 'Azules'),
            ('6', 'Morados y Violetas'),
            ('7', 'Marrones'),
            ('8', 'Grises y Neutros'),
            ('9', 'Negros'),
            ('10', 'Blancos'),
        ],
        string="Color Category",
        help="Filter colors by category"
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

    @api.onchange('category_filter_color')
    def _onchange_category_filter_color(self):
        """Filter colors based on the selected category."""
        if self.category_filter_color:
            return {'domain': {'id_color': [('category', '=', self.category_filter_color)]}}
        else:
            return {'domain': {'id_color': []}}
