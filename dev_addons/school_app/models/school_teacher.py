from odoo import api, fields, models

class SchoolTeacher(models.Model):
    _name ='school.teacher'
    _description = 'Teacher'
    name = fields.Char(string='Nombre del Profesor', required=True)
    profile = fields.Text(string='Perfil', required=True)
    subject_ids = fields.One2many(
        'school.subject', compute='_compute_subjects', readonly=False)
    
    def _compute_subjects(self):
        for teacher in self:
            teacher.subject_ids = [
                (0, 0, {'name': 'Matematicas'}), 
                (0, 0, {'name': 'Ingles'})]
