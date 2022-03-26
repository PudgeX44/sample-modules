# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    spokentoclient = fields.Boolean('Spoken to Client',required=True)