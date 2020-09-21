import pprint
import requests

url = "https://api.github.com/users/wrightrocket/repos"

payload = {}
headers = {
  'Authorization': 'git: https://github.com/ on X751S at 15-Aug-2020 14:24',
  'Accept': 'application/vnd.github.v3+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

response = response.text.encode('utf8')

pprint.pprint(response)
