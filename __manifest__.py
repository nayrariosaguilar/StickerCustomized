# -*- coding: utf-8 -*-
{
    'name': "StickerCustomized",

    'summary': """
        En aquest modul podrás crear y eliminar un Sticker personalizat""",

    'description': """
        Aprendre a un mòdul a Odoo
    """,

    'author': "Nadie",
    'website': "https://campus.proven.cat/course/view.php?id=268",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'icon': '/StickerCustomized/static/description/icon.png',
    # any module necessary for this one to work correctly
    'depends': ['base','sale','product'],

    # always loaded
    #Desactivem la gestió d'usuaris i a nivell gràfic treballarem com a súperusuari
    'data': [
        'security/ir.model.access.csv',
	'views/videoclub_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml'],
    'installable': True,
    'application': True,
    'autoinstall': False,
}
