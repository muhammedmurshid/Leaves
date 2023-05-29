from odoo import fields, models, _, api


class LeaveAllocationDate(models.Model):
    _inherit = 'hr.leave.allocation'

    date_allocation = fields.Date(string='Date')
