import json
import requests

url = "https://api.github.com/users/wrightrocket"

payload = {}
headers = {
  'Accept': 'application/vnd.github.v3+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

response_body = json.loads(response.text.encode('utf8'))
print(json.dumps(response_body, indent=2))
