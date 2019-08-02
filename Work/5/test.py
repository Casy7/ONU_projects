from functions import get_key
import json
import requests


req = requests.get("http://api.brain.com.ua/pricelists/57/json/"+get_key()+"?full=2")
link = json.loads(req.content)["url"]
print(link)
url = link
r = requests.get(url, allow_redirects=True)
open('PriceList_short.json', 'wb').write(r.content)