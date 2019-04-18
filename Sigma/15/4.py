import requests
import json


class Planet():
    def __init__(self, **properties):
        self.__dict__.update(properties)


class People():
    def __init__(self, **properties):
        self.__dict__.update(properties)


req = requests.get('https://swapi.co/api/planets/')
# print("HTTP Status Code: " + str(req.status_code))

# list_of_planets = json_response["results"]
for planet in range(1, 40):
    req = json.loads(
        requests.get(
            'https://swapi.co/api/planets/'+str(planet)+"/").content)
    if req["name"] == "Kashyyyk":
        kashyyyk = req
        break

kashyyyk_class = Planet(**kashyyyk)
for film in kashyyyk_class.films:
    req = requests.get(film)
    film_properties = json.loads(req.content)
    # print(film_properties["title"])
    kashyyyk_class.films[kashyyyk_class.films.index(
        film)] = film_properties["title"]
# print(kashyyyk_class.__dict__)
print(kashyyyk_class.films)


req = requests.get('https://swapi.co/api/people/')
# print("HTTP Status Code: " + str(req.status_code))
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
# print(obi_van_class.__dict__)
# TODO
for film in obi_van["films"]:
    req = requests.get(film)
    film_properties = json.loads(req.content)
    # print(film_properties["title"])
    obi_van["films"][obi_van["films"].index(film)] = film_properties["title"]
print(obi_van["films"])

check_particip = False
for film in kashyyyk_class.films:
    if film in obi_van["films"]:
        check_particip = True
if(check_particip) is True:
    print(obi_van_class.name,
          "принимал участие в фильме, в котором появилась планета Kashyyyk")
else:
    print(obi_van_class.name,
          "не принимал участие в фильме, в котором появилась планета Kashyyyk")


for people in range(1, 140):
    req = json.loads(
        requests.get(
            'https://swapi.co/api/people/'+str(people)+"/").content)
    if "name" in req and req["name"] == "Boba Fett":
        boba = req
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
          "принимал участие в фильме, в котором появилась планета Kashyyyk")
else:
    print(boba_class.name,
          "не принимал участие в фильме, в котором появилась планета Kashyyyk")

print(kashyyyk_class.__dict__)
print(obi_van_class.__dict__)
print(boba_class.__dict__)
final_dict_to_planet = kashyyyk_class.__dict__
final_dict_to_planet.update(obi_van_class.__dict__)
final_dict_to_planet.update(boba_class.__dict__)
final_planet = Planet(**final_dict_to_planet)
