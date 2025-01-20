# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StickersMaterial(models.Model):
    _name = 'stickers.material'
    _description = "Materials for stickers"
    name = fields.Char(string="Material Name", size=255, required=True, help="Name of the material")

class StickersShape(models.Model):
        _name = 'stickers.shape'
        _description = "Shapes available for stickers"
        name = fields.Selection(
            [("1", "Rectangle"), ("2", "Square"), ("3", "Circle"), ("4", "Star"), ("5", "Triangle"), ],
            string="Selection")

class StickersColor(models.Model):
    _name = 'stickers.color'
    _description = "Colors available for stickers"
    color_name = fields.Char(string="Color Name", size=255, required=True, help="Name of the color", default="Blanco")

class ColorCategory(models.Model):
    _name = 'stickers.color.category'
    _description = "Categories available for colors"
    category_name = fields.Selection(
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
        string="Finish Type",
        required=True,
        help="Select the type of finish of your sticker"
    )
    id_color = fields.Many2one(
        'stickers.color',
        string="Color of the Sticker",
        help="Choose the color of the Sticker"
    )

class StickersScale(models.Model):
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


class StickersCustomized(models.Model):
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
