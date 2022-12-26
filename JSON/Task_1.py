"""
Выведите из файла character.json Имя персонажа, родную планету и список эпизодов в которых он появлялся.
"""


import json

with open('character.json', 'r') as file:

    data = json.load(file)
    print(data)


def get_info(name, planet):
    print(
        f"Персонаж: {name}. Родная планета: {planet} \nЭпизоды с персонажем: ")
    for i in data["episode"]:
        print(f"- {i}")


name = data["name"]
planet = data["origin"]["name"]

get_info(name, planet)
