from random import randint
import time


class Shararam():
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

Krosh = Shararam("Крош", 120, 15, "Морковка", 30, "Уши")
print(Krosh.info())

Kopatuch = Shararam("Копатыч", 100, 18, "Лопата", 40, "Соломенная шляпа")
Kopatuch.info()

print(Krosh.strike(Kopatuch))

