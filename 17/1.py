import python_jsonschema_objects as pjs
import requests
import json

planetData = requests.get('https://swapi.co/api/planets/1')
planetSchemaData = requests.get('https://swapi.co/api/planets/schema')

planetJson = json.loads(planetData.content)

schema = json.loads(planetSchemaData.content)
builder = pjs.ObjectBuilder(schema)
classList = builder.build_classes()
PlanetClass = classList.Planet

somePlanet = PlanetClass()

somePlanet = PlanetClass(**planetJson)
print(somePlanet.__str__)
