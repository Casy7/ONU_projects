import requests
import json

import functions

url = "https://api.brain.com.ua/products/content/"+functions.get_key()
req = requests.post(url, data={"productIDs": [1,87,765]})
#                                 'password':
#                                 "b6f19093a07cdf6e2fe098d7aee90b2f"})
# req = requests.post(url)
diction = json.loads(req.content)
final_list = diction['result']['list']
print(diction['result'])
diction["result"]