# coding: utf-8
from odoo import api, models, fields, _
from odoo.exceptions import UserError, AccessError, ValidationError
import unicodedata

class SaleOrderTerm(models.Model):
    _inherit = 'sale.order'

    @api.onchange('payment_term_id')
    def _payment_term(self):
        if not self.env.user.change_payment_method and self.payment_term_id  != self.partner_id.property_payment_term_id and not self.payment_term_id.ok_in_sale:
            return {
                'value': {
                    'payment_term_id': self.partner_id.property_payment_term_id,
                },
                'warning': {
                    'title': u'Permission error',
                    'message': u'You are not authorized to change the payment method'
                }
            }