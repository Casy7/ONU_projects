# TODO Create function "get_product" wich gets properties by ID

import requests
import json
import dicttoxml

import functions

SID = functions.get_key()
# print(functions.get_IDs())
# print(functions.get_props(525078, SID))
# functions.good_view(525078)
print(functions.get_categories(SID))
functions.good_view(functions.get_props(47, SID))

example_ssd = functions.category_to_json(1484, SID)
xml = dicttoxml.dicttoxml(example_ssd).decode("utf-8")
xml.replace("<root>","")
xml.replace("</root>","")
with open("Z:/Repositories/testrepo1/Work/1/xml_example.xml",
          "w",
          encoding="UTF8") as write_file:
    write_file.write(xml)
