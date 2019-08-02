import requests
import json
import xlwt


URL = "https://api.brain.com.ua/"   # Константа домена сайта
with open('table_of_categories.json', "r") as read_file:
    cat_list = json.load(read_file)
with open('cats_by_name.json', "r") as read_file:
    cats_by_name = json.load(read_file)

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


def good_view(props, SID):
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
    category_way = find_way(int(props["categoryID"]), SID=SID)
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
    result_list.extend(get_all_images(props['productID'], get_key()))
    # Свойства
    # TODO
    properties = props['options']

    for propty in properties:
        if propty['name'] != "Гарантия, мес":
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
        props = good_view(get_props(product_ID, SID), SID)
        # TODO statistics()
        name = "rootID"
        dict_of_info[name] = props
    return dict_of_info


def ids_to_list(list_of_IDs, SID):
    list_of_info = []
    c = 0    
    ids = list_of_IDs
    length = len(ids)
    for product_ID in ids:
        props = good_view(get_props(product_ID, SID), SID)
        # TODO statistics()
        max_len = max(20000, length)
        list_of_info.append(props)
        c += 1
        print(str(round(c/max_len*100, 2))+"%")
        if c == max_len:
            return list_of_info
            break
    return list_of_info


def category_to_list(category_number, SID):
    list_of_info = get_IDs_of_category(category_number, SID)
    return ids_to_list(list_of_info, SID)


def set_price(price, recommended_price=None, exchange_rates=27):
    poss_price_1 = price*exchange_rates*1.15
    if recommended_price is not None:
        to_return = max(poss_price_1, recommended_price)
    else:
        to_return = poss_price_1
    return round(to_return, 2)


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


def get_ways(SID=None, file_name="js_categories.json"):
    req = requests.get(
        "http://api.brain.com.ua/categories/"+SID)
    json_all = json.loads(req.content)["result"]
    with open(file_name, "w", encoding = "UTF8") as write_file:
        json.dump(json_all, write_file)

    return json_all


def find_way(category_number=1484, list_of_ids="", SID=get_key()):
    if list_of_ids == "":
        try:
            with open('js_categories.json', "r") as read_file:
                list_of_ids = json.load(read_file)
        except:
            list_of_ids = get_ways(SID)
    str_out = ""
    now_id = category_number
    for category in list_of_ids:
        if category['categoryID'] == now_id:
            str_out = category['name']
            parent_id = category['parentID']
            break
    while parent_id != 1:
        for category in list_of_ids:
            if category['categoryID'] == parent_id:
                str_out = category['name']+" > "+str_out
                parent_id = category['parentID']
    # str_out = str_out[:-2]
    # list_final = str_out.split(" > ")
    # list_final.reverse()
    # print(" > ".join(list_final))
    return str_out


def category_code_to_name(code):
    return cat_list[str(code)][0]


def category_name_to_code(name):
    return cats_by_name[name][0]


def numb_of_category(name, list_of_ids="", SID=get_key()):
    if list_of_ids == "":
        try:
            with open('js_categories.json', "r") as read_file:
                list_of_ids = json.load(read_file)
        except:
            list_of_ids = get_ways(SID)
    str_out = ""
    for category in list_of_ids:
        if category['name'] == name:
            str_out = category['categoryID']
            break
    return str_out


def check_category_existing(name, list_of_ids="", SID=get_key()):
    if list_of_ids == "":
        try:
            with open('js_categories.json', "r") as read_file:
                list_of_ids = json.load(read_file)
        except:
            list_of_ids = get_ways(SID)
    str_out = ""
    for category in list_of_ids:
        if category['name'] == name:
            str_out = category['categoryID']
            break
    return str_out


def read_pricelist():
    with open('PriceList_short.json', "r",encoding="UTF8") as read_file:
        PRICELIST = tuple(json.load(read_file).values())
    tuplist_IDs_cats = []
    for product in PRICELIST:
        tuplist_IDs_cats.append((product['ProductID'],product['CategoryID']))
    tuplist_IDs_cats.sort(key = lambda x: x[1])
    return tuplist_IDs_cats


# 
# def get_product(ID, SID):


# def props_to_table(props, line):
#     with open("Z:\Repositories\testrepo1\Work\1\xl_test.xls","a")

# print(get_all_images(292663, get_key()))
