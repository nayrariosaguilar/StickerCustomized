# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Table for materials
class StickersMaterial(models.Model):
    """Material used for stickers"""
    _name = 'stickers.material'
    _description = "Materials for stickers"

    name = fields.Char(string="Material Name", size=255, required=True, help="Name of the material")
    material_type = fields.Char(string="Material Type", size=255, required=True, help="Type of the material")


# Table for shapes
class StickersShape(models.Model):
    """Shape of the sticker"""
    _name = 'stickers.shape'
    _description = "Shapes available for stickers"

    name = fields.Char(string="Shape Name", size=255, required=True, help="Name of the shape")


# Table for colors
class StickersColor(models.Model):
    """Color options for stickers"""
    _name = 'stickers.color'
    _description = "Colors available for stickers"

    color_name = fields.Char(string="Color Name", size=255, required=True, help="Name of the color")


# Table for scales
class StickersScale(models.Model):
    """Scales available for stickers"""
    _name = 'stickers.scale'
    _description = "Scales available for stickers"

    name = fields.Char(string="Scale Name", size=255, required=True, help="Name of the scale")


class StickersPrinting(models.Model):
    _name = 'stickers.printing'
    _description = "Printing types available for stickers"

    name = fields.Selection(
        [
            ('glossy', 'Glossy'),
            ('matte', 'Matte'),
            ('transparent', 'Transparent'),
            ('embossed', 'Embossed'),
            ('holographic', 'Holographic'),
        ],
        string="Finish Type",
        required=True,
        help="Select the type of finish of your sticker"
    )

# Table for customized stickers
class StickersCustomized(models.Model):
    """Customized sticker details"""
    _name = 'stickers.customized'
    _description = "Details of customized stickers"

    id_finish = fields.Many2one(
        'stickers.printing',
        string="Printing Type",
        help="Type of printing for the sticker"
    )
    id_color = fields.Many2many(
        'stickers.color',
        string="Colors",
        help="Colors used for the sticker"
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
        help="Materials used for the sticker"
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
        "Personalized Message",
        help="Custom message for the sticker"
    )
    image_personalized = fields.Text(
       "Personalized Image",
        help="Description of the custom image for the sticker"
    )
