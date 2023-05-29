from odoo import fields, models, api
import requests


class LogicLeaves(models.Model):
    _inherit = 'hr.leave'

    @api.model
    def create(self, vals):
        ss = self.env['res.groups'].search([])
        dd = self.env['res.users'].search([])
        admin_number = []
        approver_number = []

        # for i in ss:
        #     if i.category_id.name == 'Time Off':
        #         if i.name == 'All Approver':
        #             for j in i.users:
        #                 print(j.id, 'yes')
        #                 for k in dd:
        #                     if j.id == k.id:
        #                         admin_number.append(k.employee_id.work_phone)
        #                         # print(k.employee_id.work_phone, 'yes')
        #         if i.name == 'Administrator':
        #             for j in i.users:
        #                 print(j.id, 'yes')
        #                 for k in dd:
        #                     if j.id == k.id:
        #                         approver_number.append(k.employee_id.work_phone)
                                # print(k.employee_id.work_phone, 'yes')
        # admin = ' '.join(admin_number)
        # approve = ' '.join(approver_number)
        #
        # print(admin, 'admin')
        # print(approve, 'approve')
        admin_hr = '9048625264'
        hr_pro = '78564378'
        user = 'HR Manager'
        message_applied = "Hi " + user + ", an employee has requested leave in Logic HRMS. For more details login to https://corp.logiceducation.org"
        dlt_applied = '1107168381905841814'
        url = "http://sms.mithraitsolutions.com/httpapi/httpapi?token=adf60dcda3a04ec6d13f827b38349609&sender=LSMKCH&number=" + admin_hr + "&route=2&type=Text&sms=" + message_applied + "&templateid=" + dlt_applied
        # A GET request to the API
        response = requests.get(url)
        # Print the response
        response_json = response.json()
        url = "http://sms.mithraitsolutions.com/httpapi/httpapi?token=adf60dcda3a04ec6d13f827b38349609&sender=LSMKCH&number=" + hr_pro + "&route=2&type=Text&sms=" + message_applied + "&templateid=" + dlt_applied
        response = requests.get(url)
        response_json = response.json()
        print(response_json)
        return super(LogicLeaves, self).create(vals)

    # @api.model
    def action_approve(self):
        dlt_approved = '1107168381862190105'
        emp_name = []
        emp_phone = []
        emp_phone.append(self.employee_id.work_phone)
        emp_name.append(self.employee_id.name)
        employee_name = ' '.join(emp_name)
        message_approved = "Hi " + str(employee_name) + ", Your leave request in Logic HRMS has been approved by the HR Managers."

        number = ' '.join(emp_phone)
        print(number, 'subaash')
        url = "http://sms.mithraitsolutions.com/httpapi/httpapi?token=adf60dcda3a04ec6d13f827b38349609&sender=LSMKCH&number=" + str(number) + "&route=2&type=Text&sms=" + message_approved + "&templateid=" + dlt_approved

        # A GET request to the API
        response = requests.get(url)

        # Print the response
        response_json = response.json()
        return super(LogicLeaves, self).action_approve()

    def action_refuse(self):
        emp_name = []
        emp_phone = []
        emp_phone.append(self.employee_id.work_phone)
        emp_name.append(self.employee_id.name)
        employee_name = ' '.join(emp_name)
        message_rejected = "Hi " + str(employee_name) + ", Your leave request in Logic HRMS has been rejected by the HR Managers."
        dlt_rejected = '1107168381868385017'
        number = ' '.join(emp_phone)
        print(number, 'subaash')
        url = "http://sms.mithraitsolutions.com/httpapi/httpapi?token=adf60dcda3a04ec6d13f827b38349609&sender=LSMKCH&number=" + str(number) + "&route=2&type=Text&sms=" + message_rejected + "&templateid=" + dlt_rejected
        response = requests.get(url)
        response_json = response.json()
        return super(LogicLeaves, self).action_refuse()

