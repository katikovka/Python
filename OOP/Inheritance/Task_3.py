"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""


class SpaceObject():
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, size, bright):
        super().__init__(size)
        self.bright = bright

    def shine(self):
        print(f"Светит с яркостью {self.bright}")


class Planet(SpaceObject):
    def __init__(self, pop, add):
        self.pop = pop
        self.add = add

    def add_after(self, ears):
        self.pop += self.add * ears
        print(f"Спустя {ears} лет население на планете будет {self.pop} человек.")


Luna = Star(200, "7 из 10")
Luna.shine()

laplandia = Planet(22, 5)
laplandia.add_after(5)



