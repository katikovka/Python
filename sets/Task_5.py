"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
6
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]



all_lan_arr = []
res_2 = {}

res_1 = set()

students = int(input("Количество школьников: "))
while students > 0:
    n = int(input("Количество школьников с общим языком: "))
    new_lan = set()
    for i in range(n):
        s = input("Язык: ")
        new_lan.add(s)
        if s in res_2:
            res_2[s] += 1
        else:
            res_2[s] = 1
        students = students - 1
    all_lan_arr.append(new_lan)
    res_1 = res_1 | new_lan

print(res_1)
print(list(filter(lambda x: res_2[x] == len(all_lan_arr), res_2.keys())))

"""
new_lan = set()
all_lan = set()
one_lan = set()
students = int(input("Количество школьников: "))

while students > 0:
    n = int(input("Количество школьников с общим языком: "))
    students = students - n
    for i in range(n):
        lan = input("Язык: ")
        new_lan.add(lan)
        all_lan.add(lan)
        one_lan = all_lan & new_lan

print(all_lan, one_lan)
