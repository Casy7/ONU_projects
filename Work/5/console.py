import csv
import functions

def import_all_pricelist():
    pass

def import_category(category):
    

    example_ssd = functions.category_to_list(
        functions.numb_of_category(category), SID=SID)
    with open("import_2.csv", "w", encoding="UTF8") as write_file:
        writer = csv.writer(write_file, delimiter=',')
        for line in example_ssd:
            writer.writerow(line)

    


import_category("Канелярия")