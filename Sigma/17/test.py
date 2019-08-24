import python_jsonschema_objects as pjs
import requests
import json

planetData = requests.get('https://swapi.co/api/planets/1') # Получаем данные по планете в json формате
planetSchemaData = requests.get('https://swapi.co/api/planets/schema') # Получаем схему класса Planet

planetJson = json.loads(planetData.content) 

schema = json.loads(planetSchemaData.content) # Парсим схему в строку
builder = pjs.ObjectBuilder(schema) # создаем билдер для класса Planet
classList = builder.build_classes() # создаем объект класса Planet
PlanetClass = classList.Planet

somePlanet = PlanetClass(name="Tatooine")
print(somePlanet.__str__)