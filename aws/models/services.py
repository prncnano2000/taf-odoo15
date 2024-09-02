from odoo import models, fields


class AwsServices(models.Model):
    _name = 'aws.services'
    _description = 'Your services'


    name = fields.Char(required=True)

    service_id = fields.Char('service ID', required=True)

    description = fields.Selection([('cat1', 'storage'),('cat2', 'serverles'),('cat3', 'compute'),('cat4', 'Ml or AI')], string='Categorie', default='cat1', required=True)

    description_service = fields.Text()

    image = fields.Binary(required=True)
