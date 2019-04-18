import python_jsonschema_objects as pjs
import requests
import json
from pprint import pprint


def fix_scheme(json_scheme):
    for prop in json_scheme['properties']:
        item = json_scheme['properties'][prop]
        if item['type'] == 'array':
            item['items'] = {"type": "string"}


planetSchemaData = requests.get('https://swapi.co/api/planets/schema')
peopleSchemaData = requests.get('https://swapi.co/api/people/schema')


schema_for_planet = json.loads(planetSchemaData.content)
schema_for_people = json.loads(peopleSchemaData.content)
fix_scheme(schema_for_people)
fix_scheme(schema_for_planet)

builder_people = pjs.ObjectBuilder(schema_for_people)
builder_planet = pjs.ObjectBuilder(schema_for_planet)
classList_peolpe = builder_people.build_classes()
classList_planet = builder_planet.build_classes()

PlanetClass = classList_planet.Planet
PeopleClass = classList_peolpe.People


def search_planet(planet_name):
    next_page = "https://swapi.co/api/planets/"
    sought_for_planet = None
    while next_page is not None:
        req = requests.get(next_page).json()
        try:
            list_on_page = req["results"]
        except KeyError:
            break
        for planet in list_on_page:
            if planet["name"] == planet_name:
                sought_for_planet = planet
                break
        if sought_for_planet is not None:
            break
        if "next" in req:
            next_page = req["next"]
        else:
            next_page = None
    return sought_for_planet


def search_people(name):
    next_page = "https://swapi.co/api/people/"
    sought_for_person = None
    while next_page is not None:
        req = requests.get(next_page).json()
        try:
            list_on_page = req["results"]
        except KeyError:
            break
        for person in list_on_page:
            if person["name"] == name:
                sought_for_person = person
                break
        if sought_for_person is not None:
            break
        if "next" in req:
            next_page = req["next"]
        else:
            next_page = None
    return sought_for_person


def check_participation(person, planet):
    participation = False
    for film in planet.films:
        if film in person.films:
            participation = True
        if(participation) is True:
            print(person.name,
                  "принимал участие в фильме, в котором " +
                  "появилась планета Kashyyyk")
            return True
        else:
            print(person.name,
                  "не принимал участие в фильме, в " +
                  "котором появилась планета Kashyyyk")
            return False


'''for f in tatooine.films:
    content = json.loads(requests.get(f).content)
    print(content["title"])'''

# kashyyyk_class = Planet(**search_planet("Kashyyyk"))
kashyyyk_class = PlanetClass(**search_planet("Kashyyyk"))

obi_van = search_people("Obi-Wan Kenobi")
boba = search_people("Boba Fett")

# obi_van_class = People(**obi_van)
obi_van_class = PeopleClass(**search_people("Obi-Wan Kenobi"))
# boba_class = People(**boba)
boba_class = PeopleClass(**search_people("Boba Fett"))

check_participation(obi_van_class, kashyyyk_class)
check_participation(boba_class, kashyyyk_class)


print(kashyyyk_class.__dict__, "\n")
print(obi_van_class.__dict__, "\n")
print(obi_van_class.films[0], "\n")
print(boba_class.__dict__, "\n")
print(boba_class.films, "\n")
pprint(vars(kashyyyk_class))
# def dump(obj):
#     for attr in dir(obj):
#         print("obj.%s = %r" % (attr, getattr(obj, attr)))
# dump(kashyyyk_class)
