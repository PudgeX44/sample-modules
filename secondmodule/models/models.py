# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Item(models.Model):
    _name = 'secondmodule.course'
    _description = "Second Module Data"

    name = fields.Char(string="Title",required=True)
    description = fields.Text()