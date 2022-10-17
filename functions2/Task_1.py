"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def none(par1, par2, par3):
    if par1 != "None":
        print(par1)
    if par2 != "None":
        print(par2)
    if par3 != "None":
        print(par3)
    else:
        print("None")


par1 = input("Введите первый параметр: ")
par2 = input("Введите второй параметр: ")
par3 = input("Введите третий параметр: ")
none(par1, par2, par3)

