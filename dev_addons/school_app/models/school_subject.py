from odoo import api, fields, models

class SchoolSubject(models.Model):
    _name ='school.subject'
    _description = 'Curso'
    name = fields.Char(string='Nombre del Curso', required=True)
    credits = fields.Integer('Creditos')
    max_students= fields.Integer('Maximo de Alumnos')
    active = fields.Boolean()
    student_ids = fields.Many2many(comodel_name='res.partner', relation="school_subject_student", column1="student_id", column2="subject_id")
    teacher_id =  fields.Many2one('school.teacher', string='Profesor que lo dicta', required=True)
