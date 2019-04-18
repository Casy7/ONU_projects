import json
data = {"actor":{"name":"John Snow","movie":"Game of Thrones"}}
with open ("Json.json","w") as file:
    json.dump(data,file)

result = json.dumps(data, indent = 4)
print(result)