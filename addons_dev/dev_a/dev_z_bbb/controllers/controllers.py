# -*- coding: utf-8 -*-
# from odoo import http


# class DevZBbb(http.Controller):
#     @http.route('/dev_z_bbb/dev_z_bbb', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_z_bbb/dev_z_bbb/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_z_bbb.listing', {
#             'root': '/dev_z_bbb/dev_z_bbb',
#             'objects': http.request.env['dev_z_bbb.dev_z_bbb'].search([]),
#         })

#     @http.route('/dev_z_bbb/dev_z_bbb/objects/<model("dev_z_bbb.dev_z_bbb"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_z_bbb.object', {
#             'object': obj
#         })
