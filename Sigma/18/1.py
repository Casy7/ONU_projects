import json


h = {}
with open("‪D:\Git repository\Sigma\18\country_codes.json", "r") as file:
    country_info = json.loads(file)
for i in country_info.keys():
    country_info[i].pop("divisions")
    h[i] = country_info[i]
with open("‪D:\Git repository\Sigma\18\country_codes.json", "w") as write_file:
    json.dump(h, write_file)
