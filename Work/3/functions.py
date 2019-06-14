import requests
import json
import xlwt

import categories


URL = "https://api.brain.com.ua/"   # Константа домена сайта


def get_key():
    """Функция возвращает ключ сессии"""

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
    result_list = []
    rules = [
        "productID",
        "name",
        "product_code",
        "articul",
        "price",
        "brief_description",
        "description",
        "warranty",
    ]
    for rule in rules:
        try:
            result_list.append(props[rule])
        except:
            result_list.append("")
    result_list[4] = set_price(float(result_list[4]))
    # Путь категории
    category_way = categories.find_way(int(props["categoryID"]))
    result_list.append(category_way)
    # Производитель
    manufacturer = ""
    try:
        for propty in props['options']:
            if propty['name'] == "Производитель":
                manufacturer = propty['value']
                break
    except:
        pass
    result_list.append(manufacturer)
    # Фотографии (5)
    result_list.extend(get_all_images(props['productID'],get_key()))
    # Свойства
    # TODO
    properties = props['options']

    for propty in properties:
        if propty['name']!="Гарантия, мес":
            result_list.append(propty['name'])
            result_list.append(propty['value'])
 
    print("done")
    return result_list


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
    for product_ID in get_IDs_of_category(category_number, SID):
        props = good_view(get_props(product_ID, SID))
        # TODO statistics()
        name = "rootID"
        dict_of_info[name] = props
    return dict_of_info



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


def set_price(price, recommended_price = None, exchange_rates = 27):
    poss_price_1 = price*exchange_rates*1.15
    if recommended_price is not None:
        to_return = max(poss_price_1, recommended_price)
    else:
        to_return = poss_price_1
    return round(to_return,2)


def get_all_images(ID, SID):
    req = requests.get(URL + "product_pictures/" +
                                   str(ID)+"/"+SID).content
    list_of_images = json.loads(req)["result"]
    res_list = []
    for number_of_image in range(5):
        try:
            res_list.append(list_of_images[number_of_image]['large_image'])
        except IndexError:
            res_list.append('')
    return res_list
    # TODO
# def get_product(ID, SID):


# def props_to_table(props, line):
#     with open("Z:\Repositories\testrepo1\Work\1\xl_test.xls","a")

# print(get_all_images(292663, get_key()))
