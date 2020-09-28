import requests
import json
import os

# 
# ИНДИКАТОР ЗАГРУЗКИ СЕРВЕРА РЕЗУЛЬ
# 
#  



API_URL = "https://cabinet-bak.osvitavsim.org.ua/profile/requests"

while True:
    try:
        result = requests.get(API_URL)
        print(result.status_code)
        if result.status_code == 200:
            
            print(result.__dict__["_content"])
            
            f= open("guru99.html","w+")
            f.write(str(result.content))
            f.close()
            os.system("start "+f.name)
            break
    except:
        print('DDOS attack')