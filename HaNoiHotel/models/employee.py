from odoo import api, fields, models
from datetime import date


class Employee(models.Model):
    _name = 'x.employee'

    name = fields.Char(string='Name')
    dob = fields.Date(string='Date of Birth')
    regency = fields.Selection(selection=[('receptionist', 'Receptionist'), ('housekeeping', 'Housekeeping'),
                                          ('manager', 'Manager')], string='Position')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')