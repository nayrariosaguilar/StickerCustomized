# -*- coding: utf-8 -*-

from odoo import models, fields, api

       
#Taula amb els films  
class stickers_material(models.Model):
    """materials for sticker"""
    _name = 'stickers.material'
    _description = "materials for sticker"

    name = fields.Char(string="Name of the material", size=255, required=True, help='Name of the material')
    material_type  = fields.Char(string="Type of the material", size=255, required=True, help='Type of the material')

#Taula amb els films
class stickers_shape(models.Model):
    """materials for sticker"""
    _name = 'stickers.shape'
    _description = "Name of the shape"

    name  = fields.Char(string="Name of the shape", size=255, required=True, help='Name of the shape')

