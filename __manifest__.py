# -*- encoding: utf-8 -*-
{

    'name': 'Odoo - Medical Management',
    'version': '11.4',
    'author': 'Al Khidma Systems',
    'sequence': 10,
    'category': 'Generic Modules/Others',
    'depends': ['base', 'pragtech_dental_management'
                ],
    'description': """
This modules includes Medical Management Features
""",
    'website': 'http://www.alkhidmasystems.com',
    "data": [
     
        # 'security/ir.model.access.csv',


        # 'data/dashboard_data.xml',
        'views/xpath.xml',
        
    ],
    'active': False,
    # 'images': ['images/main_screenshot.png'],
    'qweb': [
        # 'static/src/xml/perio_base.xml',
        # 'static/src/xml/colorwidget.xml',
        # 'static/src/xml/chart_discount.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
