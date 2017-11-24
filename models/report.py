from odoo import models, fields, api

class marking(models.Model):
    _name = 'marking.assignment'

    name = fields.Char()
    description = fields.Text()
    date = fields.Date()

    assignment_total = []

    @api.multi
    def generate(self):
        assignment_tot = []
        # get all the marks that submitted by student
        assignment = self.env['assignment.grading'].search([])
        for marks in assignment.obtain_marks   