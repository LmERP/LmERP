# -*- coding: utf-8 -*-
# from odoo import http


# class DevZAaa(http.Controller):
#     @http.route('/dev_z_aaa/dev_z_aaa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_z_aaa/dev_z_aaa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_z_aaa.listing', {
#             'root': '/dev_z_aaa/dev_z_aaa',
#             'objects': http.request.env['dev_z_aaa.dev_z_aaa'].search([]),
#         })

#     @http.route('/dev_z_aaa/dev_z_aaa/objects/<model("dev_z_aaa.dev_z_aaa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_z_aaa.object', {
#             'object': obj
#         })
