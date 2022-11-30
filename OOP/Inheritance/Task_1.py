"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""

from random import randint
import time


class Shararam():           # Shararam == Hero
    def __init__(self, name, health, power, skill, weapon, weapon_type):
        self.name = name
        self.health = health
        self.power = power
        self.skill = skill
        self.weapon = weapon
        self.weapon_type = weapon_type

    def info(self):
        print(f"| {self.name} |")
        print(f"Здоровье: {self.health}")
        print(f"Урон: {self.power}")
        print(f"Оружие: {self.skill}")
        print(f"Броня: {self.weapon_type}")

    def strike(self, enemy):
        print("\n----- НАЧАЛО БОЯ ------\n")
        print((f"{self.name} нападает на {enemy.name}"))
        while (enemy.health > 0) or (self.health > 0):
            time.sleep(2)
            pow = randint(5, self.power + 1)
            print(f"{enemy.name} получил урон -{pow}")
            enemy.weapon -= pow
            if enemy.weapon < 0:
                enemy.health += enemy.weapon
                if enemy.health <= 0:
                    print(f"XXX {enemy.name} потерпел поражение XXX")
                    break
                enemy.weapon = 0
            else:
                print(f"Его броня упала до {enemy.weapon}")
            print(f"Здоровье: {enemy.health}")
            time.sleep(1)
            pow = randint(5, enemy.power + 1)
            print(f"{self.name} получил урон -{pow}")
            self.weapon -= pow
            if self.weapon < 0:
                self.health += self.weapon
                if self.health <= 0:
                    print(f"XXX {self.name} потерпел поражение XXX")
                    break
                self.weapon = 0
            else:
                print(f"Его броня упала до {self.weapon}")
            print(f"Здоровье: {self.health}")
            print("_"*20)
        print(f"Бой окончен")


class Magician(Shararam):
    def __init__(self, name, health, power, skill, weapon, weapon_type):
        super().__init__(name)
        super().__init__(health)
        super().__init__(power)
        super().__init__(skill)
        super().__init__(weapon)
        super().__init__(weapon_type)

    def hello(self):
        self.info()
        print(f"-----| Поприветствуем {self.name} |-----")
        time.sleep(2)

    def attack(self, weapon_type):
        print(f"{self.name} атакует {weapon_type}")
