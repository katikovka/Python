"""
Напишите список функций по требованию. Пользователь вводит имя.
Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""

name = input("Введите имя:\n")
test = [lambda name: name + " гений", lambda name: name + " сверхразум ", lambda name: "Просто " + name]
gen = ['а', 'я', 'г', 'м']
over = ['о', 'ь', 'л', 'н']
if name[-1] in gen:
    print(test[0](name))
elif name[-1] in over:
    print(test[1](name))
else:
    print(test[2](name))