import json
class Person():
    def __init__(self,firstName,lastName,hobbies,age,children):
        self.firstName = firstName
        self.lastName = lastName
        self.hobbies = hobbies
        self.age = age
        self.children = children
john = Person (
    firstName="Jane",
    lastName="Doe",
    hobbies = ["running", "sky diving", "singing"],
    age=35,
    children=[
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
)
dict_of_pers = john.__dict__
with open ("Json.json","w") as file:
    json.dump(dict_of_pers,file)

result = json.dumps(dict_of_pers, indent = 4)
print(result)