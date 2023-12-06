odoo.define('pos_order_receipt_customization.client_name', function(require) {
    'use strict';

    var { Order } = require('pos_of_sale.models');
    var Registries = require('pos_of_sale.Registries');

    const CustomOrder = (Order) => class CustomOrder extends Order {
        export_for_pricing(){
            var result = super.export_for_pricing(...arguments);
            result.client = this.get_partner();          
            return result;
        };
    };
    Registries.Model.extend(Order, CustomOrder);
});
