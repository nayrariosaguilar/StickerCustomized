# -*- coding: utf-8 -*-

from odoo import models, fields, api

       
#Taula amb els films  
class stickers_material(models.Model):
    """materials for sticker"""
    _name = 'stickers.material'
    _description = "materials for sticker"

    name = fields.Char(string="Name of the material", size=255, required=True, help='Name of the material')
    material_type  = fields.Char(string="Type of the material", size=255, required=True, help='Type of the material')

#Taula amb les formes
class stickers_shape(models.Model):
    """shape of the sticker"""
    _name = 'stickers.shape'
    _description = "Name of the shape"
    name  = fields.Char(string="Name of the shape", size=255, required=True, help='Name of the shape')

#Taula amb els films
class stickers_shape(models.Model):
    """materials for sticker"""
    _name = 'stickers.shape'
    _description = "Name of the shape"
    name  = fields.Char(string="Name of the shape", size=255, required=True, help='Name of the shape')

#scale
class stickers_scale(models.Model):
    """materials for sticker"""
    _name = 'stickers.scale'
    name  = fields.Char(string="Name of the scale", size=255, required=True, help='Name of the scale')

#printing
class stickers_printing(models.Model):
    """materials for sticker"""
    _name = 'stickers.printing'
    _description = "Type of printing"
    name = fields.Char(string="Type of printing", size=255, required=True, help='Type of printing')

#Taula amb els films
class stickers_shape(models.Model):
    """materials for sticker"""
    _name = 'stickers.shape'
    _description = "Name of the shape"
    id_finish  = fields.Many2One(string="Name of the shape", size=255, required=True, help='Name of the shape')
    id_color   = fields.Many2Many(string="Name of the shape", size=255, required=True, help='Name of the shape')
    id_scale   = fields.Many2One(string="Name of the shape", size=255, required=True, help='Name of the shape')
    id_shape   = fields.Many2One(string="Name of the shape", size=255, required=True, help='Name of the shape')
    id_material  = fields.Many2many(string="Name of the shape", size=255, required=True, help='Name of the shape')
    width  = fields.Integer(string="Name of the shape", size=255, required=True, help='Name of the shape')
    message_personalized  = fields.Text("Message", help="Personalized Message")
    image_personalized  = fields.Text("Image", help="Description of the category")
    height  = fields.Integer(string="Name of the shape", size=255, required=True, help='Name of the shape')