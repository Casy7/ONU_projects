# TODO Create function "get_product" wich gets properties by ID

import requests
import json
import dicttoxml
import csv
import functions

SID = functions.get_key()
# print(functions.get_IDs())
# print(functions.get_props(525078, SID))
# functions.good_view(525078)
print(functions.get_categories(SID))
functions.good_view(functions.get_props(47, SID), SID)

example_ssd = functions.category_to_list(1484, SID)

with open("import_2.csv", "w", encoding="UTF8") as write_file:
    writer = csv.writer(write_file, delimiter=',')
    for line in example_ssd:
        writer.writerow(line)
