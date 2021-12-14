card = '''
{
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.2",
    "body": [
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": 2,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Chatbot de ServiceNow",
                            "weight": "Bolder",
                            "size": "Medium",
                            "wrap": true,
                            "style": "heading"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Por favor introduzca la siguiente información y con gusto le ayudaré a abrir el tiquete:",
                            "isSubtle": true,
                            "wrap": true
                        },
                        {
                            "type": "Container",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Descripción corta",
                                    "wrap": true
                                },
                                {
                                    "type": "Input.Text",
                                    "id": "short_description",
                                    "placeholder": "Descripción corta"
                                }
                            ]
                        },
                        {
                            "type": "Container",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Descripción",
                                    "wrap": true
                                },
                                {
                                    "type": "Input.Text",
                                    "id": "description",
                                    "placeholder": "Descripción",
                                    "isMultiline": true
                                }
                            ]
                        },
                        {
                            "type": "Container",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Categoría",
                                    "wrap": true
                                },
                                {
                                    "type": "Input.ChoiceSet",
                                    "choices": [
                                        {
                                            "title": "Network",
                                            "value": "network"
                                        },
                                        {
                                            "title": "Hardware",
                                            "value": "hardware"
                                        },
                                        {
                                            "title": "Software",
                                            "value": "software"
                                        },
                                        {
                                            "title": "Database",
                                            "value": "database"
                                        }
                                    ],
                                    "placeholder": "Categoría",
                                    "id": "category"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "Column",
                    "width": 1,
                    "items": [
                        {
                            "type": "Image",
                            "url": "https://www.aedcr.com/sites/default/files/styles/logo_empresa/public/logo_bcr_valores_sitio_web.png?itok=wc3tC6uG"
                        }
                    ]
                }
            ]
        }
    ],
    "actions": [
        {
            "type": "Action.Submit",
            "title": "Submit"
        }
    ]
}
'''