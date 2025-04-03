# -*- coding: utf-8 -*-

from odoo import models, fields #, api

class TestModel(models.Model):
    _name = "test_model"
    _description = "This is a simple test model."

    name = fields.Char()

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Estate Proprty model."

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')],
        help="Garden orientation on cradinal points")
# class real_estate(models.Model):
#     _name = 'real_estate.real_estate'
#     _description = 'real_estate.real_estate'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

