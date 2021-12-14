from webexteamssdk import WebexTeamsAPI
from flask import Flask, request

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
        api.messages.create(roomId = room_id, text = '¡Hola ' + person.nickName + '! ¿Cómo estás? Mi nombre es ' + me.displayName + ' y estoy para ayudarte.')
    
    return "Success"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8085)