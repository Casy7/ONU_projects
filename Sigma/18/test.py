import requests
import json

country_code = "gt"
LINK = 'https://holidayapi.com/countries/'
final_link = LINK+country_code
country_info = requests.get("https://holidayapi.com/v1/holidays?key=4ab4a939-43af-40d7-b8ba-b38f107646cf&country=US&year=2018")
country_info = json.loads(country_info.content)
holidays = country_info["holidays"]
print(holidays)

# 
"""
import requests
import json


country_code = "gt"
LINK = 'https://holidayapi.com/countries/'
final_link = LINK+country_code
country_info = requests.get(final_link)
country_info = json.loads(country_info.content)
print(country_info)

"""
