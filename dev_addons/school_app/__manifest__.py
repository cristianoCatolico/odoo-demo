{
    'name': "Cursos",
    'summary': """
    Gestionar curso, estudiantes y profesores
    """,
    'description': """
    Agrega nuevos modelos de curso, estudiantes y profesores
    """,
    'author': "Martin Lozano",
    'website': "",
    'category': 'School',
    'version': '1.0',
    'depends': [
        'base',
    ],
    'data': [
        'security/school_security.xml',
        'security/ir.model.access.csv',
        'views/school_teacher_views.xml',
        'views/school_student_views.xml',
        'views/school_subject_views.xml',
        'views/menu_item_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}