"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""


class Duck():
    def sound(self):
        return "кря-кря"

    def dress(self):
        return "я не могу носить одежду"


class Human():
    def sound(self):
        return "*имитация кряканья*"

    def dress(self):
        return "я ношу одежду"


human = Human()
dack = Duck()

for animal in (human, dack):
    print(animal.sound())
    print(animal.dress())
