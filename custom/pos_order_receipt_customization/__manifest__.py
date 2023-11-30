{
    'name': 'POS receipt customization',
    'category': 'customization',
    "depends": ['product'],
    "data": [
            'views/product_extension.xml',   
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_order_receipt_customization/static/src/js/**/*',
            'pos_order_receipt_customization/static/src/xml/**/*',
        ],
    },
    'installable': True,
}