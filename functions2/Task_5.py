"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""


def HEX(colour):
    colour = colour.lstrip('#')
    clr = len(colour)
    return tuple(int(colour[i:i + clr // 3], 16) for i in range(0, clr, clr // 3))


first = input("Для начала ввидите 'цвета'\nДля выхода 'Q'\n ")
ans = []
while True:
    if first == 'Q':
        break
    elif first == "цвета":
        hex = input("Введите HEX цвета: ")
        rgb = HEX(hex)
        print("Ваш цвет", rgb)
    else:
        print("Нет такой команды")
    first = input("Для начала ввидите 'цвета'\nДля выхода 'Q'\n ")
