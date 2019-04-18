import python_jsonschema_objects as pjs
import requests
import json


class Planet():
    def __init__(self, **properties):
        self.__dict__.update(properties)


class People():
    def __init__(self, **properties):
        self.__dict__.update(properties)


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


def fix_scheme(json_scheme):
    for prop in json_scheme['properties']:
        item = json_scheme['properties'][prop]
        if item['type'] == 'array':
            item['items'] = {"type": "string"}


planetRequest = requests.get('https://swapi.co/api/planets/1')
planetSchemaData = requests.get('https://swapi.co/api/planets/schema')

schema = json.loads(planetSchemaData.content)
fix_scheme(schema)

builder = pjs.ObjectBuilder(schema)
classList = builder.build_classes()
PlanetClass = classList.Planet
somePlanet1 = json.loads(planetRequest.content)
tatooine = PlanetClass(**somePlanet1)
print(tatooine.name)


for f in tatooine.films:
    content = json.loads(requests.get(f).content)
    print(content["title"])


kashyyyk_class = Planet(**search_planet("Kashyyyk"))


for film in kashyyyk_class.films:
    req = requests.get(film)
    film_properties = json.loads(req.content)
    kashyyyk_class.films[kashyyyk_class.films.index(
        film)] = film_properties["title"]
    print(kashyyyk_class.films)


obi_van = search_people("Obi-Wan Kenobi")
boba = search_people("Boba Fett")

obi_van_class = People(**obi_van)
boba_class = People(**boba)

print(obi_van)
dict_to_class = {}


for film in obi_van["films"]:
    req = requests.get(film)
    film_properties = json.loads(req.content)
    obi_van["films"][obi_van["films"].index(film)] = film_properties["title"]
    print(obi_van["films"])

check_participation(obi_van_class, kashyyyk_class)
check_participation(boba_class, kashyyyk_class)

print(kashyyyk_class.__dict__)
print(obi_van_class.__dict__)
print(boba_class.__dict__)

final_dict_to_planet = kashyyyk_class.__dict__
final_dict_to_planet.update(obi_van_class.__dict__)
final_dict_to_planet.update(boba_class.__dict__)
final_planet = Planet(**final_dict_to_planet)
