import json

with open("WhereAmI.json", "r") as file:
    data = json.load(file)

for line in data.keys():
    if "Odessa" not in data.valueline]:
        print(line,": ", data[line],sep="")
    else:
        data[line]="Kiew"