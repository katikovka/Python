"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».
Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""


def amount_ball(ball):
    if 0 <= ball <= 49:
        print("Скидка 10%")
    elif 50 <= ball <= 99:
        print("Скидка 15%")
    elif ball >= 100:
        print("Скидка 20%")


ball = int(input("Введите количество баллов:"))
while ball != 0:
    amount_ball(ball)
    ball = int(input("Введите количество баллов:"))