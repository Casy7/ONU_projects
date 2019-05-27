import requests
import json
import xlwt

workbook1 = xlwt.Workbook()
tabl = workbook1.add_sheet('Test')

with open("Z:/Repositories/testrepo1/Work/1/get1.json", "r",
          encoding="UTF-8") as file:
    json_file = json.load(file)
number_of_errors = 0
tabl.write(0, 0, "id")
tabl.write(0, 1, "Title")
tabl.write(0, 2, "Content")
for numb in range(len(json_file)):
# for numb in range(50):
    try:
        current_definition = json_file[str(numb+2)]
        digit = 0
        list_of_props = ["CategoryID", "Name", "Description"]
        for i in range(len(list_of_props)):
            tabl.write(numb-number_of_errors+1, i,
                       current_definition[list_of_props[i]])
        digit += 1
    except:
        number_of_errors += 1
        print("error\n")
        pass

workbook1.save('Z:/Repositories/testrepo1/Work/1/xl_rec_1.xls')
