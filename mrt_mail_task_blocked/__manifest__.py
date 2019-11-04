# -*- coding: utf-8 -*-
{
    'name': 'Task Blocked Mail',
    'version': '12.0.1.0.0',
    'category': 'Addon',
    'sequence': 1,
    'summary': "Sends a mail when a task is blocked",
    'description': "Sends an e-mail when a task is set to blocked.",
    'author': 'Tiago Magrini Rigo',
    'website': '',
    'depends': ['base','project'],
    'data': [
        'data/mail_template.xml',
    ],
    'images':['static/description/task_blocked_cover.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': [],
}
