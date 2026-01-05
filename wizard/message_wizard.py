from odoo import fields, models

class MessageWizard(models.TransientModel):
    _name = "message.wizard"
    _description = "Wizard to display messages"

    name = fields.Text(
        string="Message",
        readonly=True,
        default=lambda self: self.env.context.get("message", False),
    )
