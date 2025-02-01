from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'material'
    _description = 'Materiales para fabricación de stickers'
    _inherits = {'product.template': 'product_template_id'}

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
    ubicacion_almacen = fields.Char(string="Ubicación en almacén")

    # Cantidad disponible en stock (obtenida de product.template)
    cantidad_disponible = fields.Float(
        string="Cantidad disponible",
        compute="_compute_cantidad_disponible",
        store=True
    )

    # Se mantiene solo m² como unidad, sin conversión en este modelo
    cantidad_en_m2 = fields.Float(
        string="Cantidad en m²",
        compute="_compute_cantidad_m2",
        store=True
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

