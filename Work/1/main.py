import requests
import json
import xlwt

import functions

SID = functions.get_key()
# print(functions.get_IDs())
print(functions.get_props(525078, SID))
functions.good_view(525078)
