import requests
import json


URL = "https://api.brain.com.ua/"   # Константа домена сайта


def get_key():
    """Функция получает ключ сессии"""

    url = "https://api.brain.com.ua/auth"
    req = requests.post(url, data={"login": "casy@zest.com.ua",
                                   'password':
                                   "b6f19093a07cdf6e2fe098d7aee90b2f"})
    diction = json.loads(req.content)
    return diction["result"]


def get_categories(SID):
    req = requests.get(URL+"/categories/"+SID)
    dict_of_categories = json.loads(req.content)["result"]
    return dict_of_categories


def get_IDs():
    # TODO Путь сделать относительным!
    with open("Z:/Repositories/testrepo1/Work/1/get1.json",
              "r",
              encoding="UTF-8") as file:
        json_file = json.load(file)

    list_of_IDs = []
    for prop in json_file.keys():
        list_of_IDs.append(prop)
    return list_of_IDs


def get_props(ID, SID):
    req = requests.get(URL + "/product/" + str(ID) + "/" + SID)
    props = json.loads(req.content)
    return props["result"]


def good_view(props):
    dict_good_props = {}
    dict_good_props["Название"] = props["name"]
    dict_good_props["Описание"] = props["description"]
    dict_good_props["Цена, $"] = props["price"]
    dict_good_props["Цена, UAH"] = props["price_uah"]
    dict_good_props["Короткое описание"] = props["brief_description"]
    options = props["options"].keys()
    new_options = {}
    counter = 0

    for option in options:
        new_options[option["name"]] = option["value"]
        counter += 1
    main_props.update(new_options)
    print(main_props)


def get_ID(product):
    return product["productID"]


def get_IDs(products_list):
    list_of_IDs = []
    for product in products_list:
        list_of_IDs.append(product["productID"])
    return list_of_IDs
# def get_product(ID, SID):


# def props_to_table(props, line):
#     with open("Z:\Repositories\testrepo1\Work\1\xl_test.xls","a")
