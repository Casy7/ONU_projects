import requests
import json

import functions
def get_ways(file_name="js_categories.json"):
      req = requests.get("http://api.brain.com.ua/categories/"+functions.get_key())
      json_all = json.loads(req.content)["result"]
      with open(file_name,
            "w",
            encoding="UTF8") as write_file:
      json.dump(json_all, write_file)
      