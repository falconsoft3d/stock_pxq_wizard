# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class PxQWizard(models.TransientModel):
    _name = "pxq.wizard"
    _description = "Asistente PxQ"

    product_ids = fields.Many2many('product.product', string='Productos')

    @api.multi
    def update_standard_price(self):
        quant_obj = self.env['stock.quant']
        for rec in self:
            for product in rec.product_ids:
                quants = quant_obj.search([('product_id','=',product.id)])
                value = sum(x.inventory_value for x in quants)
                qty = sum(x.qty for x in quants)
                if qty > 0.0:
                    product.standard_price = value/qty
