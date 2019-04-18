import python_jsonschema_objects as pjs
import requests
import json

planetRequest = requests.get('https://swapi.co/api/planets/1')
planetSchemaData = requests.get('https://swapi.co/api/planets/schema')


def fix_scheme(json_scheme):
    for prop in json_scheme['properties']:
        item = json_scheme['properties'][prop]
        if item['type'] == 'array':
            item['items'] = {"type": "string"}


schema = json.loads(planetSchemaData.content)
fix_scheme(schema)

builder = pjs.ObjectBuilder(schema)
classList = builder.build_classes()
PlanetClass = classList.Planet
somePlanet1 = json.loads(planetRequest.content)
tatooine = PlanetClass(**somePlanet1)
print(tatooine.name)

for f in tatooine.films:
    print(f)
