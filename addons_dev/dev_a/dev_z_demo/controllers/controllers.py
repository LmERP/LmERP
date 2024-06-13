# -*- coding: utf-8 -*-
# from odoo import http


# class DevZDemo(http.Controller):
#     @http.route('/dev_z_demo/dev_z_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_z_demo/dev_z_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_z_demo.listing', {
#             'root': '/dev_z_demo/dev_z_demo',
#             'objects': http.request.env['dev_z_demo.dev_z_demo'].search([]),
#         })

#     @http.route('/dev_z_demo/dev_z_demo/objects/<model("dev_z_demo.dev_z_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_z_demo.object', {
#             'object': obj
#         })
