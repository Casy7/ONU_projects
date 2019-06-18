import requests
import json
import pprint


def get_country_code(country):
    with open("‪country_codes.json", "r") as json_with_codes:
        dict_of_codes = json.load(json_with_codes)

    country_code = dict_of_codes[country]
    return country_code


def create_link(country_code):
    link = "https://holidayapi.com/v1/holidays?key=4ab4a939-43" + \
        "af-40d7-b8ba-b38f107646cf&country="+country_code+"&year=2018"
    return link


def change_date_format(date):
    date = date[-5:]
    date = date[3:5]+"."+date[:2]
    return date


country = "United States"   # "Ukraine", "Turkey", "Zimbabwe" etc.

country_info = requests.get(create_link(get_country_code(country)))
country_info = json.loads(country_info.content)
holidays = country_info["holidays"]

for holiday in holidays:
    holiday.pop("observed")
    holiday["date"] = change_date_format(holiday["date"])


pp = pprint.PrettyPrinter(indent=2, width=150)
pp.pprint(holidays)

with open("‪country_holidays.json", "w") as write_file:
    json.dump(holidays, write_file, indent=4, sort_keys=True)
