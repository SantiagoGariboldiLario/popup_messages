from odoo import fields, models

class MessageWizard(models.TransientModel):
    _name = "message.wizard"
    _description = "Wizard to display messages"

    def _get_default(self):
        if self.env.context.get("message", False):
            return self.env.context.get("message")
        return False

    name = fields.Text(
         string="Message",
         readonly=True,
         default=_get_default)
