from tkinter import *
# import tkMessageBox
import tkinter
import json

def find_leafs(cat):
    with open('js_categories.json', "r") as read_file:
        tree = json.load(read_file)
    ignore = []
    leafs = []
    for category in tree:
        parent_id = category["parentID"]
        temp_cat = category
        
        temp_way = []
        is_leaf = False
        if temp_cat["parentID"]==1:
            ignore.append(temp_cat["parentID"])
        while temp_cat["parentID"]!=1:
            if temp_cat not in ignore:
                if temp_cat==cat:
                    is_leaf = True
                    leafs.append(temp_cat)
                    break
                temp_way.append(temp_cat)

                temp_cat = temp_cat["parentID"]
            else:
                ignore.extend(temp_way)
                break

find_leafs(1331)    