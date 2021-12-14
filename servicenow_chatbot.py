from webexteamssdk import WebexTeamsAPI
from flask import Flask, request
from servicenow_card import card
import json
import requests
import os

app = Flask(__name__)
api = WebexTeamsAPI()

@app.route('/webhook', methods=['POST'])
def webhook():
    me = api.people.me()
    data = request.get_json()
    person_id = data['data']['personId']
    
    if person_id != me.id:
        message_id = data['data']['id']
        room_id = data['data']['roomId']
        
        person = api.people.get(person_id)
        message = api.messages.get(message_id)
        attachment = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": json.loads(card)
        }
        api.messages.create(roomId=room_id, text="Este texto se verá si la tarjeta no se puede mostrar", attachments=[attachment])
    
    return "Success"

@app.route('/cards', methods=['POST'])
def cards():
    data = request.get_json()
    message_id = data["data"]["id"]
    room_id = data['data']['roomId']
    person_id = data['data']['personId']
    person = api.people.get(person_id)

    url = "https://api.ciscospark.com/v1/attachment/actions/" + message_id

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + os.environ["WEBEX_TEAMS_ACCESS_TOKEN"]
        }

    response = requests.request("GET", url, headers=headers)

    res = json.loads(response.text)
    payload = {
        "description": res["inputs"]["description"],
        "short_description": res["inputs"]["short_description"],
        "category": res["inputs"]["category"],
        "caller_id": "abraham.lincoln@example.com" #TO DO: usar el email de la persona
    }

    url = "https://dev90052.service-now.com/api/now/table/incident"
    username = os.environ["SERVICENOW_USERNAME"]
    password = os.environ["SERVICENOW_PASSWORD"]

    data = json.dumps(payload)

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, auth=(username, password), headers=headers, data=data)

    data = response.json()
    if response.status_code == 201:
        ticket_number = data['result']['number']
        api.messages.create(roomId = room_id, markdown = '## Fue creado exitosamente en ServiceNow el tiquete número ' + ticket_number)
    else:
        api.messages.create(roomId = room_id, text = 'Sucedió un error al crear el tiquete. Por favor intente después')

    return "success"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8085)