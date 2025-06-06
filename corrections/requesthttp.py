import json

import requests

url = "http://localhost:8000/vol/199QFA"
response = requests.get(url)
d = json.loads(response.text)
print(response)
print(d)