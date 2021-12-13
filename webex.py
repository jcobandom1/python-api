import requests
import json

url = "https://webexapis.com/v1/messages"
token = "Y2IzM2FhYzMtZWJlOC00ODJhLTllMWItYjlhZTBiNDlhYWU2NmI3YmE2YzQtMjYx_PF84_2a001399-4e85-4adc-b568-32f8032f2ae7"
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