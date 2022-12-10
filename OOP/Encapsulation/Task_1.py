"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму (сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""


class BankAccount():
    def __init__(self, name, balance, pasport):
        self._name = name
        self.__balance = balance
        self.__pasport = pasport

    def getpasport(self):
        return self.__pasport

    def getbalance(self):
        return self.__balance

    def setnumbpasp(self):
        inp = input("Введите пароль:")
        newpasport = input("Введите новый номер паспорта: ")
        password = "olegesthleb"
        if password == inp:
            self.__pasport = newpasport
            return "Номер паспорта изменён."
        else:
            return "Неверный пароль."


    def setbalance(self):
        newbalance = input("Введите желаемый баланс: ")
        if newbalance < 0:
            return "Невалидный баланс."
        else:
            self.__balance = newbalance


    def delnumbpas(self):
        inp = input("Введите пароль:")
        password = "olegesthleb"
        if password == inp:
            del self.__pasport
            return "Паспортные данные удалены.."
        else:
            return "Неверный пароль."


Oleg = BankAccount("Олег", 150, 56345190)

print(Oleg.getpasport())
print(Oleg.getbalance())