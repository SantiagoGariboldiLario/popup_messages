{
    "name": "Popup Message",
    "author": "Eynes SRL",
    "website": "https://www.eynes.com.ar",
    "category": "Tools",
    "summary": "Create message box wizard",
    "description": """This module is useful to create a custom popup message.""",
    "version": "19.0.1.0.0",
    "depends": ["base"],
    "license": "AGPL-3",
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "wizard/message_wizard.xml",
    ],
    "auto_install": False,
    "installable": True,
}
