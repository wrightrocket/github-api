#!/usr/bin/env python
__author__='Keith Wright'
'''
Create a request to get information about the GitHub API endpoints for a user

Get all the information from a request, parse it with the module for JSON, and
and loop through the dictionary to find URLs which are endpoints for the API.

Here is an example of public data that the request used obtains as the body:

{
    "login": "wrightrocket",
    "id": 931144,
    "node_id": "MDQ6VXNlcjkzMTE0NA==",
    "avatar_url": "https://avatars0.githubusercontent.com/u/931144?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/wrightrocket",
    "html_url": "https://github.com/wrightrocket",
    "followers_url": "https://api.github.com/users/wrightrocket/followers",
    "following_url": "https://api.github.com/users/wrightrocket/following{/other_user}",
    "gists_url": "https://api.github.com/users/wrightrocket/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/wrightrocket/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/wrightrocket/subscriptions",
    "organizations_url": "https://api.github.com/users/wrightrocket/orgs",
    "repos_url": "https://api.github.com/users/wrightrocket/repos",
    "events_url": "https://api.github.com/users/wrightrocket/events{/privacy}",
    "received_events_url": "https://api.github.com/users/wrightrocket/received_events",
    "type": "User",
    "site_admin": false,
    "name": "WrightRocket",
    "company": null,
    "blog": "",
    "location": null,
    "email": null,
    "hireable": null,
    "bio": null,
    "twitter_username": null,
    "public_repos": 353,
    "public_gists": 13,
    "followers": 2,
    "following": 5,
    "created_at": "2011-07-21T21:19:56Z",
    "updated_at": "2020-09-22T03:28:18Z"
}

This is a large JSON text object, where the endpoints have keys the end with "_url".
Once the json module converts the text into a Python dictionary, this can be used
to isolate the endpoints or API locations that are "exposed".

The GitHub REST API documentation can be explored at: https://docs.github.com/en/rest
'''
import json
import requests

url = "https://api.github.com/users/wrightrocket"

payload = {}
headers = {
  'Accept': 'application/vnd.github.v3+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

json_text = response.text.encode('utf8')

python_dict = json.loads(json_text)

print(json.dumps(python_dict, indent=2, sort_keys=True))

# Create a variable to store a dictionary containing the parsed JSON text

''' Without "with"
f = open('user.txt', 'w')
try:
  f.write(json_text)
finally:
  f.close()
'''
endpoints_list = [] # create an empty dict to store endpoint URLS

for git_key in python_dict.keys():
    if git_key.endswith("_url") and "api.github" in python_dict[git_key]:
        url_value = python_dict[git_key]
        print("Endpoint: {0} added with URL: {1}".format(git_key, url_value))
        endpoints_list.append(url_value)

print("\nList of user's GitHub API endpoints:", endpoints_list)

# instead of doing requests one by one you could do a list of them by using a function

def git_request(url, headers=headers, data=payload):
    rest_response = requests.request("GET", url, headers=headers, data=data)
    json_text = response.text.encode('utf8')    
    py_dict = json.loads(json_text)
    return py_dict

def json_pretty(json_dict, indent=2, sort_keys=True):
    print(json.dumps(json_dict, indent=2, sort_keys=True))

for url in endpoints_list:
    json_pretty(git_request(url))
    
