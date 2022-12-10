list1 = []
while True:
    mark = input("Введите оценку: ")
    if mark != 0:
        list1.append(mark)
    else:
        break
marks = 0
for i in list1:
    marks += mark.count(i)
print(mark, len(marks), marks / len(marks) * 100)
