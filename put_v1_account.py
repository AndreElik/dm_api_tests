import requests

url = "http://5.63.153.31:5051/v1/account/564e9e0e-3232-4f00-ac72-056f616aabd6"

payload = {}
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
