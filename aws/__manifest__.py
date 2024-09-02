# -*- coding: utf-8 -*-
{
    'name': 'theme_aws',
    'description': 'your homme theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/aws_services.xml',
        'views/snippets/explore-services.xml',
        'views/snippets/snippets.xml',
        'views/header.xml',
        'views/footer.xml'
    ],
    'assets':{
        'web.assets_frontend': [
        '/aws/static/src/js/explore-services.js',
        ],
    },
    'images': [
        '/aws/static/src/img/snippets/city1.png',
    ],
    'snippet_lists': {
    },

    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
