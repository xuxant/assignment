# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class assignment(models.Model):
#     _name = 'assignment.assignment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class teacher(models.Model):
    _name = 'teacher.info'
    _rec_name = 'teacher_name'


    teacher_name = fields.Char('Name', required=True)
    teacher_course = fields.Char('Subject', requied=True)
    teacher_faculty = fields.Char('Faculty', required=True)

class home(models.Model):
    _name = 'home.info'


class batch(models.Model):
    _name = 'batch.info'
    _rec_name = 'batch_name'

    batch_name = fields.Char('Class Name', required=True)
    student_number = fields.Integer('Number Of Student', required=True)
    batch_teacher = fields.Many2one('teacher.info', 'Class Teacher')


class student(models.Model):
    _name = 'student.info'
    _rec_name = 'student_name'


    student_name = fields.Char('Name', required=True)
    student_level = fields.Selection([('1', 'Primary Level'), ('2', 'Secondary level'), ('3', 'High School Level'), ('4', 'Bachelor level'), ('5', 'Master Level')])
    batch_name = fields.Many2one('batch.info', 'Class Name')
    student_course = fields.Char('Course', required=True)



class assignment(models.Model):
    _name = 'assignment.info'
    _rec_name = 'assignment_name'


    assignment_subject = fields.Char('Subject Name', required=True)
    assignment_name = fields.Char('Assignment Name', required=True)
    start_date = fields.Date('Start date', required=True)
    dead_line = fields.Date('Deadline', required=True)
    teacher_name = fields.Many2one('teacher.info', 'AssignedBy')
    assignment_subject = fields.Many2one('subject.info', 'Subject', teacher_name="[('teacher_name','=',teacher_name)]")
    batch_name = fields.Many2one('batch.info', 'AssignedTo')




class grading(models.Model):
    _name = 'assignment.grading'
    _rec_name = 'total_marks'


    student_name = fields.Many2one('student.info', 'Assignment Submitted By', required=True)
    assignment_name = fields.Many2one('assignment.info', 'Name Of Assignment', required=True)
    submitted_date = fields.Date('Submitted Date', required=True)
    marks_avaliable = fields.Integer('Total Marks For Assignment', required=True)
    content_completed = fields.Integer('Complition in Percentage', required=True)
    peer_marks = fields.Integer('Peer Assigned Marks', required=True)
    teacher_marks = fields.Integer('Teacher Assigned Marks', required=True)
    total_marks = fields.Integer(string='Total Marks', store=True, compute='_total_calculation')



    @api.depends('content_completed', 'peer_marks', 'teacher_marks')
    def _total_calculation(self):
        for total in self:
            total.total_marks = total.peer_marks + total.teacher_marks
            return total.total_marks




class subject(models.Model):
    _name = 'subject.info'
    _rec_name = 'subject_name'

    batch_name = fields.Many2one('batch.info', 'Class Name', requied=True)
    subject_name = fields.Char('Subject Name', required=True)
    subject_teacher = fields.Many2one('teacher.info', 'Teacher Name')


class marking(models.Model):
    _name = 'marking.assignment'
    _res_name = 'totol_marks'

    student_name = fields.Many2one('student.info', 'Student Name')
    marks_assignment = fields.Many2one('assignment.grading', 'Marks Assignment')
    grade = fields.Char('Grade', requied=True)





   # prod_obj=self.pool.get(product.product) prod_name=prod_obj.browse(cr,uid,ids)[0].name