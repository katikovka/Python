"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
import json
task = ["oleg", 24, ["Belarus", "Russia"]]
di = {"name": "oleg", "age": 24, "countries": ["Belarus", "Russia"]}
with open('Babchonok_Oleg_2.json', 'w') as fp:
    json.dump(di, fp)

a = [1, 2, 3]
k = tuple
d = {1: 'a',
     2: 'b',
     3: 'c'}
m = set()
m = {1, 6, 4, 8, 3}

num = 100
div = 10

while div > -11:
    div -= 1
    if div == 0:
        break
    print(num / div)
else:
    print("не было break")
