from odoo import models, fields, api

class subjects(models.Model):
    _name = 'subjects.info'
    _rec_name = 'subject_name'

    subject_name = fields.Char('Subject Name', required=True)
    