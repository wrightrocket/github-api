import json
import requests

url = "https://api.github.com/repos/wrightrocket/github-api"

payload = {}
headers = {
  'Authorization': 'git: https://github.com/ on X751S at 15-Aug-2020 14:24',
  'Accept': 'application/vnd.github.v3+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(json.dumps(json.loads(response.text.encode('utf8')), indent=2))

