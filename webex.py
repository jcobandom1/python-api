import requests
import json
import os

url = "https://webexapis.com/v1/messages"
token = os.environ["WEBEX_TEAMS_ACCESS_TOKEN"]
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

payload = {
  "roomId": room_id,
  "text": "Enviado desde Python"
}

data = json.dumps(payload)

headers = {
  "Authorization": "Bearer " + token,
  "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=data)

print(response.text)