from datetime import timedelta
from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string="Property Name", required=True)
    description = fields.Text(string="Description")
    date_availability = fields.Date(
        string="Available From",
        copy=False,
        default=lambda self: fields.Date.context_today(self) + timedelta(days=90)
    )
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    postcode = fields.Char(string="Postcode")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation"
    )
    living_area = fields.Integer(string="Living Area")
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        string="Status",
        default='new'
    )
