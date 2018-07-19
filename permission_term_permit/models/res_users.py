# coding: utf-8
from odoo import _, api, fields, models

class ResUsersPayment(models.Model):
    _inherit = 'res.users'

    change_payment_method = fields.Boolean('Change the payment method', translate=True)
