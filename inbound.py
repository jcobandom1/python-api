from webexteamssdk import WebexTeamsAPI
from flask import Flask, request

app = Flask(__name__)
api = WebexTeamsAPI()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    person_id = data['data']['personId']
    message_id = data['data']['id']
    room_id = data['data']['roomId']

    person = api.people.get(person_id)
    message = api.messages.get(message_id)
    room = api.rooms.get(room_id) 
    
    print(person.displayName, 'escribió el mensaje', message.text, 'en el espacio', room.title)

    return "Success"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8085)