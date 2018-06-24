# -*- coding: utf-8 -*-
{
    'name': "POS Complimentary",

    'summary': """
        Add function complimentary on point of sale""",

    'description': """
        Add function complimentary on point of sale
    """,

    'author': "Lê Thái Lộc",
    'category': 'Point of Sale',
    'version': '1.0',
    'support': 'kunkaamd@gmail.com',
    
    'images': ['static/description/description.png',
               'static/description/description1.png',
               'static/description/description2.png',
               'static/description/description3.png',
               'static/description/description4.png'],
    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],
    
    # always loaded
    'data': [
        'views/pos_complimentary.xml',
        'views/register.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
}