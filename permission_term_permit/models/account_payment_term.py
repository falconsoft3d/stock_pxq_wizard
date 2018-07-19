# coding: utf-8
from odoo import api, models, fields, _


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    ok_in_sale = fields.Boolean('User in the sale Order', translate=True)
