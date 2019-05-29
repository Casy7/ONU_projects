import requests
import json


def get_key():
    """Функция получает ключ сессии"""
    url = "https://api.brain.com.ua/auth"

    # all_products = json.loads(req.content)
    r = requests.post(url, data={"login": "casy@zest.com.ua",
                                 'password':
                                 "b6f19093a07cdf6e2fe098d7aee90b2f"})

    # print(all_products)
    diction = json.loads(r.content)
    return diction["result"]
