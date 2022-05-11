from odoo import fields, models


class InheritResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    show_wpp_icon = fields.Boolean(
        string="Show Whatsapp Icon", related="website_id.show_wpp_icon", readonly=False
    )
    wpp_number = fields.Char(
        string="WhatsApp Number", related="website_id.wpp_number", readonly=False
    )


class InheritWebsiteModule(models.Model):
    _inherit = "website"

    wpp_number = fields.Char(string="Whatsapp Number")
    show_wpp_icon = fields.Boolean(string="Show WhatsApp Icon")

    def redirect_whatsapp_url(self):
        """Returns WhatsApp Redirect URL."""
        wa_url = "https://api.whatsapp.com/send?phone=" + str(self.wpp_number)
        return wa_url
