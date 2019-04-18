import json

with open("colors.json", "r") as file:
    data = json.load(file)


for color in data["colors"]:
    print("{0} - {1}".format(color["color"], color["value"]))
