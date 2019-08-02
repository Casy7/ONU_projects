import requests
import json
import xlwt


def get_key():
    """Функция возвращает ключ сессии"""

    url = "https://api.brain.com.ua/auth"
    req = requests.post(url, data={"login": "casy@zest.com.ua",
                                   'password':
                                   "b6f19093a07cdf6e2fe098d7aee90b2f"})
    diction = json.loads(req.content)
    return diction["result"]


def UPDATE_pricelist():
    req = requests.get(
        "http://api.brain.com.ua/pricelists/57/json/"+get_key()+"?full=2")
    url = json.loads(req.content)["url"]
    print("Подгрузка прайслиста...")
    r = requests.get(url, allow_redirects=True)
    open('PriceList_short.json', 'wb').write(r.content)


def REPAIR_categories():

    def get_ways(SID=get_key(), file_name="js_categories.json"):
        print("Подгрузка недостающих файлов...")
        req = requests.get(
            "http://api.brain.com.ua/categories/"+SID)
        json_all = json.loads(req.content)["result"]
        with open(file_name, "w", encoding="UTF8") as write_file:
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

    def repair_table():
        try:
            with open('js_categories.json', "r") as read_file:
                list_of_cats = json.load(read_file)

            final_dict = {}
            dict_by_name = {}

            for category in list_of_cats:
                name = category['name']
                id = category["categoryID"]
                way = find_way(id)
                final_dict[int(id)] = (name, way)
                dict_by_name[name] = [id, way]

            with open('table_of_categories.json', "w", encoding="UTF8") as file:
                json.dump(final_dict, file)
            with open('cats_by_name.json', "w", encoding="UTF8") as file:
                json.dump(dict_by_name, file)
        except:
            get_ways()
            repair_table()
    repair_table()


def DOWNLOAD_files():
    files = ('main.py','functions.py')
    for file in files:
        req = requests.get(
            "https://raw.githubusercontent.com/Casy7/testrepo1/master/Work/5/"+file)             
        text = req.text
        print("Загрузка "+file+"...")
        with open(file, "w", encoding="UTF8") as file:
           file.write(text)



hello = "Вас приветствует установщик сей чудо-программы. Итак, вы уверены, что вам абсолютно не нужна папка, в которой находится этот файл, и вы, несмотря на то, что ЭТО писал я, готовы рискнуть и установить импортёр? (Y/N)  "
answer = input(hello).lower()
if answer == "y":
    print("Ну, если что, я не виноват.")
    REPAIR_categories()
    UPDATE_pricelist()
    DOWNLOAD_files()
    input("Ну, файлы загружены. А вот будет ли ЭТО работать, одним богам ведомо (да и то не факт). Для открытия программы запустите \"main.py\"")
else:
    input("Эээ...(если что, вы выбрали \"нет\")")
