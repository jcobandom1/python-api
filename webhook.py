from flask import Flask
import requests
import json
import os

app = Flask(__name__)
@app.route('/webhook', methods = ['POST'])
def webhook():
  url = "https://webexapis.com/v1/messages"
  data = json.dumps({
    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl",
    "text": "¡Recibimos un webhook!"
  })
  headers = {
    "Authorization": "Bearer " + os.environ["WEBEX_TEAMS_ACCESS_TOKEN"],
    "Content-Type": "application/json"
  }
  response = requests.post(url, headers=headers, data=data)
  return 'Success'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8085)