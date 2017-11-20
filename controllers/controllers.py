# -*- coding: utf-8 -*-
from odoo import http

# class Assignment(http.Controller):
#     @http.route('/assignment/assignment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assignment/assignment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('assignment.listing', {
#             'root': '/assignment/assignment',
#             'objects': http.request.env['assignment.assignment'].search([]),
#         })

#     @http.route('/assignment/assignment/objects/<model("assignment.assignment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assignment.object', {
#             'object': obj
#         })