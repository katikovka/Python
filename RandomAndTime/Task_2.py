"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.
1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""


from random import *

team1 = input("Название первой сборной: ")
team2 = input("Название второй сборной: ")
amount1 = int(input("Число участников сборной: "))
amount2 = int(input("Число участников сборной: "))

print("Пловец сборной", team1, ": ", randint(1, amount1))
print("Пловец сборной", team2, ": ", randint(1, amount2))