from odoo import http


class AwsServices(http.Controller):

    @http.route('/services/', auth="public", type="json", methods=['POST'])
    def all_services(self):
        services = http.request.env['aws.services'].search_read([], ['name', 'image', 'description'])    
        return services