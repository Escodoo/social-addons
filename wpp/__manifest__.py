# Copyright 2022 Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Wpp Standalone',
    'summary': """
        Stand-alone WhatsApp Integration""",
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Escodoo',
    'depends': ['base', 'contacts', 'website', 'sale'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/whatsapp_icon_templates.xml',
        'views/whatsapp_icon_assets.xml',
        'views/inherit_res_config_settings.xml',
        'wizard/wizard.xml',
        'wizard/message_wizard.xml',
        'wizard/wizard_contact.xml',
        'wizard/wizard_multiple_contact.xml',
        'wizard/share_action.xml',
        'security/wpp_security.xml',
    ],
    'external_dependencies': {
        'python': [
            'html2text',
        ]
    }
}
