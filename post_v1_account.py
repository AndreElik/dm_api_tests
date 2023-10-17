import requests
import json

url = "http://5.63.153.31:5051/v1/account"

payload = json.dumps({
  "login": "user_253",
  "email": "user_253@gmail.com",
  "password": "123456qwerty"
})
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
