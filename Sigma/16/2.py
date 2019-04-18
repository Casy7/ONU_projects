import requests
import json


class Planet():
    def __init__(self, **properties):
        self.__dict__.update(properties)


class People():
    def __init__(self, **properties):
        self.__dict__.update(properties)


# use pep standard and move URL to constant
# URL from constant
# get list of planets, convert them to list of planet object
planets = []
for page in range(1, 40):
    req = requests.get(
        ("https://swapi.co/api/planets/?page="+str(page))).json()

    try:
        list_on_page = req["results"]
    except KeyError:
        break

    for planet in list_on_page:
        planets.append(Planet(**planet))
        if planet["name"] == "Kashyyyk":
            kashyyyk = planet
            break

        # get films and filter collection
kashyyyk_class = Planet(**kashyyyk)

for film in kashyyyk_class.films:
    req = requests.get(film)
    film_properties = json.loads(req.content)
    kashyyyk_class.films[kashyyyk_class.films.index(
        film)] = film_properties["title"]
    print(kashyyyk_class.films)


req = requests.get('https://swapi.co/api/people/')
json_response = json.loads(req.content)

list_of_people = json_response["results"]
obi_van = None

for human in list_of_people:
    if human["name"] == "Obi-Wan Kenobi":
        obi_van = human
        break

print(obi_van)
dict_to_class = {}

for some_property in list(obi_van.keys())[0:5]:
    dict_to_class[some_property] = obi_van[some_property]

obi_van_class = People(**dict_to_class)

for film in obi_van["films"]:
    req = requests.get(film)
    film_properties = json.loads(req.content)
    obi_van["films"][obi_van["films"].index(film)] = film_properties["title"]
    print(obi_van["films"])

check_particip = False
for film in kashyyyk_class.films:
    if film in obi_van["films"]:
        check_particip = True
    if(check_particip) is True:
        print(obi_van_class.name,
              "принимал участие в фильме, в " +
              "котором появилась планета Kashyyyk")
    else:
        print(obi_van_class.name,
              "не принимал участие в фильме, " +
              "в котором появилась планета Kashyyyk")


for page in range(1, 40):
    req = requests.get(
        ("https://swapi.co/api/people/?page="+str(page))).json()
    try:
        list_on_page = req["results"]
    except KeyError:
        list_on_page = []
        break
    for human in list_on_page:
        if "name" in human and human["name"] == "Boba Fett":
            boba = human
            break


for some_property in list(obi_van.keys())[0:5]:
    dict_to_class[some_property] = boba[some_property]

boba_class = People(**dict_to_class)


check_particip = False
for film in kashyyyk_class.films:
    if film in obi_van["films"]:
        check_particip = True
    if(check_particip) is True:
        print(boba_class.name,
              "принимал участие в фильме, в котором " +
              "появилась планета Kashyyyk")
    else:
        print(boba_class.name,
              "не принимал участие в фильме, в " +
              "котором появилась планета Kashyyyk")

print(kashyyyk_class.__dict__)
print(obi_van_class.__dict__)
print(boba_class.__dict__)
final_dict_to_planet = kashyyyk_class.__dict__
final_dict_to_planet.update(obi_van_class.__dict__)
final_dict_to_planet.update(boba_class.__dict__)
final_planet = Planet(**final_dict_to_planet)
