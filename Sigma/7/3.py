#!python3
class Animal(object):
    """Создаёт милых животных"""
    health="Good"
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

hippo = Animal("Jake", 12)
monkey = Animal("Mike",3)
elephant= Animal("Nik",23)
cat = Animal("Boots", 3)

hippo.is_alive = False
hippo.health = "Critical"
print(hippo.health)

monkey.health="Dead"
elephant.health="Bad"

print(monkey.health)
print(elephant.health)
print(cat.health)


