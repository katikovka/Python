"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""
import json

task = ["oleg", 24, ["Belarus", "Russia"], (24, 1), ["Moscow", "Vladikavkaz", 'Krasnodar', "Rostov", "Nalchik"]]
di = {"name": "oleg",
      "age": 24,
      "countries": [
          {
              "name": "Belarus",
              "time": 24,
              "cities": ["Nalchik"]
          },
          {
              "name": "Russia",
              "time": 1,
              "cities": ["Moscow", "Vladikavkaz", "Krasnodar", "Rostov"]
          }
      ]}

with open('Babchonok_Oleg_3.json', 'w') as fp:
    json.dump(di, fp)
