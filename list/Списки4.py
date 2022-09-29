list1 = []
while True:
    teacher = input("Если хотите добавить наставника, введите '+' \n")
    if teacher == "+":
        name = input("1. Введите фамилию преподавателя: ")
        post = input("2. Введите должность преподавателя: ")
        students = input("2. Введите количество студентов во всех группах: ")
        list1.append([name, post, students])
    else:
        break
print(list1)