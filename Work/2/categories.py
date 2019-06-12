import requests
import json

import functions


def get_ways(file_name="js_categories.json"):
    req = requests.get(
        "http://api.brain.com.ua/categories/"+functions.get_key())
    json_all = json.loads(req.content)["result"]
    with open(file_name, "w") as write_file:
        json.dump(json_all, write_file)

    return json_all


def find_way(category_number=1484, list_of_ids=""):
    if list_of_ids == "":
        try:
            with open('js_categories.json', "r") as read_file:
                list_of_ids = json.load(read_file)
        except:
            list_of_ids = get_ways()
    str_out = ""
    now_id = category_number
    for category in list_of_ids:
        if category['categoryID'] == now_id:
            str_out += " \""+category['name']+"\" >"
            parent_id = category['parentID']
            break
    while parent_id != 1:
        for category in list_of_ids:
            if category['categoryID'] == parent_id:
                str_out += " \""+category['name']+"\" >"
                parent_id = category['parentID']
    str_out = str_out[:-2]
    list_final = str_out.split(" > ")
    list_final.reverse()
    print(" > ".join(list_final))
    return str_out


def category_code_to_name(code):
    try:
        with open('js_categories.json', "r") as read_file:
            list_of_ids = json.load(read_file)
    except:
        list_of_ids = get_ways()
    for category in list_of_ids:
        if category['categoryID'] == code:
            name = category['name']
            return name


def category_name_to_code(code):
    try:
        with open('js_categories.json', "r") as read_file:
            list_of_ids = json.load(read_file)
    except:
        list_of_ids = get_ways()
    for category in list_of_ids:
        if category['name'] == code:
            name = category['categoryID']
            return name


find_way(7682)
