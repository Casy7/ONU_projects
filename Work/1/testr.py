import requests
import json

a = requests.get(
    "http://api.brain.com.ua/filters_all/125/2111c1727bf062198c549dcfa411c5ce")
f = json.loads(a.content)
print(f)
