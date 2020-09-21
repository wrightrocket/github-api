from pprint import pprint
import requests

url = "https://api.github.com/users/wrightrocket"

payload = {}
headers = {
  'Accept': 'application/vnd.github.v3+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))
pprint(response.text)
