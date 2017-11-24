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
    teacher_contact = fields.Char('Contact Number')
    teacher_email = fields.Char('E-mail', requied=True)
    faculty = fields.Many2one('faculty.info','Faculty', required=True)



class faculty(models.Model):
    _name = 'faculty.info'
    _rec_name = 'faculty'

    faculty = fields.Char('Faculty', requied=True)
    head_of_department = fields.Char('Faculty Administrator')



class batch(models.Model):
    _name = 'batch.info'
    _rec_name = 'year'

    year = fields.Char('Academic Year', required=True)
    faculty = fields.Many2one('faculty.info', required=True)
    year_start = fields.Date('Start Date', required=True)
    year_end = fields.Date('End Date', required=True)
    student_number = fields.Integer('Number Of Student', required=True)
    batch_teacher = fields.Many2one('teacher.info', 'Class Teacher')


class subject(models.Model):
    _name = 'subject.info'
    _rec_name = 'subject_name'

    batch_name = fields.Many2one('batch.info', 'Class Name', required=True)
    subject_name = fields.Char('Subject Name', required=True)
    subject_teacher = fields.Many2one('teacher.info', 'Teacher Name')




class student(models.Model):
    _name = 'student.info'
    _rec_name = 'student_name'


    student_name = fields.Char('Name', required=True)
    roll_no = fields.Integer('Roll No.', required=True)
    contact = fields.Char('Contact Number', required=True)
    year = fields.Many2one('batch.info', 'Academic Year', required=True)
    faculty = fields.Many2one('faculty.info', 'Department' )



class assignment(models.Model):
    _name = 'assignment.info'
    _rec_name = 'assignment_name'

    
    year = fields.Many2one('batch.info', 'AssignedTo')
    assignment_name = fields.Char('Assignment Name', required=True)
    start_date = fields.Date('Start date', required=True)
    dead_line = fields.Date('Deadline', required=True)
    teacher_name = fields.Many2one('teacher.info', 'Assigned By')
    subject_name = fields.Many2one('subject.info', 'Subject', domain="[('subject_teacher','=',teacher_name)]")
    




class grading(models.Model):
    _name = 'assignment.grading'
    _rec_name = 'obtain_marks'

    @api.constrains('obtain_marks', 'minimum_marks')
    def _validate_marks(self):
        '''Method to validate marks'''
        min_mark = self.minimum_marks > self.maximum_marks
        if (self.obtain_marks > self.maximum_marks or min_mark):
            raise ValidationError(_('''The obtained marks and minimum marks
                              should not extend maximum marks!.'''))



    assignment_id = fields.Many2one('marking.assignment', 'Report')
    student_name = fields.Many2one('student.info', 'Assignment Submitted By', required=True)
    assignment_name = fields.Many2one('assignment.info', 'Name Of Assignment', required=True)
    submitted_date = fields.Date('Submitted Date', required=True)
    minimum_marks = fields.Integer("Minimum Marks",
                                 help="Minimum Marks of subject")
    maximum_marks = fields.Integer("Maximum Marks",
                                 help="Maximum Marks of subject")
    peer_marks = fields.Integer('Peer Assigned Marks', required=True)
    teacher_marks = fields.Integer('Teacher Assigned Marks', required=True)
    obtain_marks = fields.Integer("Obtain Marks", group_operator="avg", compute='_total_calculation')
  #  total_marks = fields.Integer(string='Total Marks', store=True, compute='_total_calculation')
  #  evaluation = fields.Char('Evaluation')
    result = fields.Char(compute='_evaluation_calculation', string='Result',
                         help="Result Obtained", store=True)



    @api.depends('peer_marks', 'teacher_marks')
    def _total_calculation(self):
        for obtain in self:
            obtain.obtain_marks = obtain.peer_marks + obtain.teacher_marks
            return obtain.obtain_marks

    
    @api.multi
    @api.depends('obtain_marks', 'minimum_marks')
    def _evaluation_calculation(self):
        for grade in self:
            if grade.minimum_marks and grade.obtain_marks:
                if (self.obtain_marks > self.minimum_marks):
                    grade.result = 'Pass'
                else:
                    grade.result = 'Fail'




