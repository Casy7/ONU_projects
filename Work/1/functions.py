import requests
import json
import xlwt


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


def get_IDs_by_pricelist(json_file=None):
    if json_file is None:
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
    rules = {
        "productID": "ID",
        "name": "Название",
        "articul": "Артикул",
        "product_code": "Код товара",
        "price": "Цена",
        "brief_description": "Короткое описание",
        "description": "Описание",
        "warranty": "Гарантия, мес.",
        "large_image": "Фото"
    }
    for rule in rules.keys():
        dict_good_props[rule] = rules[rule]

    main_props = {}
    for propty in dict_good_props:
        main_props[rules[propty]] = props[propty]
    options = props["options"]
    new_options = {}
    counter = 0

    for option in options:
        new_options[option["name"]] = option["value"]
        counter += 1
    main_props.update(new_options)
    print(main_props)
    return main_props


def get_ID(product):
    return product["productID"]


def get_IDs(products_list):
    list_of_IDs = []
    for product in products_list:
        list_of_IDs.append(product["productID"])
    return list_of_IDs


def get_IDs_of_category(category_number, SID):
    req_of_category = requests.get(URL + "products/" +
                                   str(category_number)+"/"+SID).content
    json_of_category = json.loads(req_of_category)["result"]["list"]
    list_of_IDs = get_IDs(json_of_category)
    return list_of_IDs


def category_to_json(category_number, SID):
    dict_of_info = []
    for product_ID in functions.get_IDs_of_category(category_number, SID):
        props = functions.good_view(functions.get_props(product_ID, SID))
        # TODO statistics()
        dict_of_info.append(props)

# def get_product(ID, SID):


# def props_to_table(props, line):
#     with open("Z:\Repositories\testrepo1\Work\1\xl_test.xls","a")
