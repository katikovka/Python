"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""


list1 = {}
list1['1'] = 1
list1['2'] = 2
list1['3'] = 3
list1['5'] = 5
list1['6'] = 6

print(list1)

element1 = list1.get('1')
element6 = list1.get('6')

list1['1'] = element6
list1['6'] = element1

print(list1)
