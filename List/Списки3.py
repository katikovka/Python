mark = input("Введите оценки через пробел: \n").split(' ')
five = 0
other = 0
for i in mark:
    if int(i) == 5:
        five = five + 1
    else:
        other = other + 1
print("Процент полученных пятёрок: ", (five*100) / len(mark))
