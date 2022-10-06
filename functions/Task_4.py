"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""


def IMT(weight, height):
    index = weight / (height * height)
    return index


def amount_IMT(index):
    if index < 18.5:
        print("Недостаточный вес")
    elif 18.5 <= index <= 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")


weight = int(input("Вес: "))
height = int(input("Рост: "))
index = IMT(weight, height)
amount_IMT(index)