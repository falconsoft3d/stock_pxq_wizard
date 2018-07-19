# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrderNotCopy(models.Model):
    _inherit = "sale.order"
    user_id = fields.Many2one('res.users', copy=False)