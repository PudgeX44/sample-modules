# -*- coding: utf-8 -*-
# from odoo import http


# class C:\users\nmr\desktop\odoo\mymodules\secondmodule(http.Controller):
#     @http.route('/c:\users\nmr\desktop\odoo\mymodules\secondmodule/c:\users\nmr\desktop\odoo\mymodules\secondmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\nmr\desktop\odoo\mymodules\secondmodule/c:\users\nmr\desktop\odoo\mymodules\secondmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\nmr\desktop\odoo\mymodules\secondmodule.listing', {
#             'root': '/c:\users\nmr\desktop\odoo\mymodules\secondmodule/c:\users\nmr\desktop\odoo\mymodules\secondmodule',
#             'objects': http.request.env['c:\users\nmr\desktop\odoo\mymodules\secondmodule.c:\users\nmr\desktop\odoo\mymodules\secondmodule'].search([]),
#         })

#     @http.route('/c:\users\nmr\desktop\odoo\mymodules\secondmodule/c:\users\nmr\desktop\odoo\mymodules\secondmodule/objects/<model("c:\users\nmr\desktop\odoo\mymodules\secondmodule.c:\users\nmr\desktop\odoo\mymodules\secondmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\nmr\desktop\odoo\mymodules\secondmodule.object', {
#             'object': obj
#         })
