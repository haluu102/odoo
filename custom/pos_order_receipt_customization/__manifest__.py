{
    "name": "POS order receipt customization",
    "version": "23.01",
    "category": "customization",
    "summary": "POS Order Receipt Customization",
    "author": "thuha",
    'website': "http://www.odooistic.co.uk/",
    "depends": ['product'],
    "data": [
            # 'views/product_extension.xml', 
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_order_receipt_customization/static/src/js/**/*',
            'pos_order_receipt_customization/static/src/xml/**/*',
        ],
    },
    "installable": True,
}