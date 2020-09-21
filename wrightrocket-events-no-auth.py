import json
import requests

url = "https://api.github.com/users/wrightrocket/received_events"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

# parse data
json_response = json.loads(response.text.encode('utf8'))

# format data

response_body = json.dumps(json_response, indent = 2)

print (response_body)
