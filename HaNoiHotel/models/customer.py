from odoo import api, fields, models


class Customer(models.Model):
    _name = 'customer'
    _inherit = 'res.partner'

    # customer_id = fields.Char(string='ID')
