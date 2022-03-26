# -*- coding: utf-8 -*-
# from odoo import http


# class C:\users\nmr\desktop\odoo\mymodules\firstmodule(http.Controller):
#     @http.route('/c:\users\nmr\desktop\odoo\mymodules\firstmodule/c:\users\nmr\desktop\odoo\mymodules\firstmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\nmr\desktop\odoo\mymodules\firstmodule/c:\users\nmr\desktop\odoo\mymodules\firstmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\nmr\desktop\odoo\mymodules\firstmodule.listing', {
#             'root': '/c:\users\nmr\desktop\odoo\mymodules\firstmodule/c:\users\nmr\desktop\odoo\mymodules\firstmodule',
#             'objects': http.request.env['c:\users\nmr\desktop\odoo\mymodules\firstmodule.c:\users\nmr\desktop\odoo\mymodules\firstmodule'].search([]),
#         })

#     @http.route('/c:\users\nmr\desktop\odoo\mymodules\firstmodule/c:\users\nmr\desktop\odoo\mymodules\firstmodule/objects/<model("c:\users\nmr\desktop\odoo\mymodules\firstmodule.c:\users\nmr\desktop\odoo\mymodules\firstmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\nmr\desktop\odoo\mymodules\firstmodule.object', {
#             'object': obj
#         })
