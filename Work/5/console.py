import csv
import functions

def import_all_pricelist():
    pass

def import_category(category):
    cat_code = functions.category_name_to_code(category)
    tuplist = functions.read_pricelist()
    with open("Exmport_File.csv", "w", encoding="UTF8") as write_file:
        writer = csv.writer(write_file, delimiter=',')
    current_ids = []
    for index in range(len(tuplist)):
        index = 0
        while tuplist[index][1] == cat_code:
            current_ids.append(tuplist[index][0])
            index+=1
        break
    print(current_ids)


    


import_category("Канелярия")