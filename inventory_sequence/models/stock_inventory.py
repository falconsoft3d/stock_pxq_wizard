# -*- coding: utf-8 -*-

from odoo import api, fields, models

class StockInventory(models.Model):
    _inherit = "stock.inventory"

    seq_name = fields.Char('Código', translate=True, default="Nuevo")

    user_id = fields.Many2one('res.users', string='Responsable', track_visibility='onchange',
                              default=lambda self: self.env.user)

    @api.model
    def create(self, vals):
        if vals.get('seq_name', "Nuevo") == "Nuevo":
            vals['seq_name'] = self.env['ir.sequence'].next_by_code('stock.inventory') or "Nuevo"
        return super(StockInventory, self).create(vals)