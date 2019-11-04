# -*- coding: utf-8 -*-
# © 2019 Mr_T - Tiago Magrini Rigo 

from odoo import api, fields, models, _

class Task(models.Model):
    _inherit = "project.task"

    kanban_state = fields.Selection(inverse='_inverse_state')

    @api.multi
    def _inverse_state(self):
        for obj in self:
            if obj.kanban_state == 'blocked':
                template = self.env['ir.model.data'].get_object('mrt_mail_task_blocked', 'email_project_task_blocked')
                template.send_mail(self.id, force_send=True)