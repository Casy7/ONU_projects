import requests
import json
import xlwt

import categories


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
        "product_code": "Код товара",
        "articul": "Артикул",
        "price_uah": "Цена",
        "brief_description": "Короткое описание",
        "description": "Описание",
        "warranty": "Гарантия, мес.",
        "large_image": "Фото"
    }
    for rule in rules.keys():
        dict_good_props[rule] = rules[rule]

    category_way = categories.find_way(int(props["categoryID"]))

    main_props = {}
    for propty in dict_good_props:
        main_props[rules[propty]] = props[propty]
    options = props["options"]
    new_options = {}
    counter = 0

    for option in options:
        new_options[option["name"]] = option["value"]
        counter += 1
    main_props["Путь"] = category_way
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
    dict_of_info = {}
    c = 0
    for product_ID in get_IDs_of_category(category_number, SID):
        props = good_view(get_props(product_ID, SID))
        # TODO statistics()
        name = "rootID"
        dict_of_info[name] = props
        c += 1
        if c == 20:
            return dict_of_info
            break


def category_to_list(category_number, SID):
    list_of_info = []
    c = 0
    for product_ID in get_IDs_of_category(category_number, SID):
        props = good_view(get_props(product_ID, SID))
        # TODO statistics()

        list_of_info.append(props)
        c += 1
        if c == 20:
            return list_of_info
            break


def get_all_images(ID, SID):
    req = requests.get(URL + "product_pictures/" +
                                   str(ID)+"/"+SID).content
    list_of_images = json.loads(req)["result"]
    res_list = []
    for number_of_image in range(5):
        try:
            res_list.append({"Фото"+str(number_of_image):list_of_images[number_of_image]['full_image']})
        except IndexError:
            res_list.append('')
    return res_list
    # TODO
# def get_product(ID, SID):


# def props_to_table(props, line):
#     with open("Z:\Repositories\testrepo1\Work\1\xl_test.xls","a")

print(get_all_images(292663, get_key()))
