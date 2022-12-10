numbers = list(map(int, input("Введите числа через пробел: \n").split(' ')))
res = True
for i in range(len(numbers)-1):
    if numbers[i] - numbers[i + 1] == -1:
        pass
    else:
        res = False
if res:
    print("Да")
else:
    print("Нет")