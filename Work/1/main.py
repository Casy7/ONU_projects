# TODO Create function "get_product" wich gets properties by ID

import requests
import json
import xlwt

import functions

SID = functions.get_key()
# print(functions.get_IDs())
# print(functions.get_props(525078, SID))
# functions.good_view(525078)
print(functions.get_categories(SID))
functions.good_view(functions.get_props(47, SID))

workbook = xlwt.Workbook()
table = workbook.add_sheet('1')
line = 1
# TODO Check this code and simplify it.
for product_ID in functions.get_IDs_of_category(1484, SID):
    props = functions.good_view(functions.get_props(product_ID, SID))
    column = 0
    for prop in props:
        table.write(line, column, prop)
        table.write(line, column+1, props[prop])
        column += 2
    line += 1


workbook.save('Z:/Repositories/testrepo1/Work/1/xl_test.xls')
