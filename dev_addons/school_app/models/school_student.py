from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name ='school.student'
    _description = 'Estudiante'
    name = fields.Char(string='Nombre del Estudiante', required=True)
    birth_date = fields.Date(string='Fecha de nacimiento del Estudiante', required=True)
    age = fields.Integer(compute='_get_age', string='Edad', help='The age of the student.')
    
    @api.onchange('birth_date')
    def _get_age(self):
        for record in self:
            if record.birth_date:
                from datetime import datetime
                today = datetime.today().date()
                age = (today.year - record.birth_date.year) - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
                record.age = age
    final_exam_grade = fields.Float(string='Nota final', required=True)
    subject_ids= fields.Many2many('school.subject')
