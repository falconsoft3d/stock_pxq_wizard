# -*- coding: utf-8 -*-

{
    'name': "Inventory Sequence MFH",
    'summary': """business_area""",
    'description': """
        Secuencia de Inventario
    """,
    'author': "Falcon Solutions SpA",
    'maintainer': 'Falcon Solutions SpA',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Account',
    'version': '10.0.1',
    'depends': ['base','l10n_cl_base',
                ],
    'data': [
         'data/ir_sequence.xml',
         'views/stock_inventory.xml',
    ],
    'demo': [
    ],
    'images': ['static/description/banner.jpg'],
}
