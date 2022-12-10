"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""

file2 = open('file_2.txt', 'w+')
file2.write("но у меня не получается")
file2 = open('file_2.txt', 'r')
text_file2 = file2.read()


file1 = open('file_1.txt', 'r')
text_file1 = file1.read()

file2_1 = open('file_1+2.txt', 'w+')

file2_1.write(text_file1 + ", " + text_file2)
