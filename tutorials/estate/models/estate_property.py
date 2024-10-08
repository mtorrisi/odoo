from odoo import fields, models

class EstatePropery(models.Model):
    _name = "estate_property"
    _description = "Property Model"

    name = fields.Char()
    description = fields.Text()