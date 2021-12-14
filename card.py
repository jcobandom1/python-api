from webexteamssdk import WebexTeamsAPI
import json

api = WebexTeamsAPI()

card = '''
{
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.2",
    "body": [
        {
            "type": "TextBlock",
            "text": "Banco de Costa Rica",
            "size": "Large",
            "weight": "Bolder"
        },
        {
            "type": "TextBlock",
            "text": "Curso Programabilidad de Red",
            "size": "Medium"
        },
        {
            "type": "Image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/LOGO_BCR.svg/2560px-LOGO_BCR.svg.png",
            "spacing": "None"
        }
    ],
    "actions": [
        {
            "type": "Action.OpenUrl",
            "title": "Abrir en navegador",
            "url": "https://bancobcr.com"
        }
    ]
}
'''

attachment = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": json.loads(card)
        }

room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

api.messages.create(roomId = room_id, text = "Texto de respaldo", attachments = [attachment])