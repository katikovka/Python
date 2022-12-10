"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)

и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).

Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""
import random


class Basic_Task:
    def __init__(self, user_name, amount_tasks, successful_tasks, points_for_tasks=1):
        self.amount_tasks = amount_tasks
        self.user_name = user_name
        self.successful_tasks = successful_tasks
        self.points_for_tasks = points_for_tasks
        self.points = points_for_tasks * successful_tasks

    def __str__(self):
        return f"{self.user_name}:{self.points}"


class All_or_Nothing(Basic_Task):

    def __init__(self, user_name, amount_tasks, successful_tasks, points_for_tasks=1):
        super().__init__(user_name, amount_tasks, successful_tasks, points_for_tasks)
        self.points = amount_tasks * points_for_tasks if amount_tasks == successful_tasks else 0


class Fast(Basic_Task):
    def __init__(self, user_name, amount_tasks, successful_tasks, points_for_tasks, time, best_time, point_for_error):
        super().__init__(user_name, amount_tasks, successful_tasks, points_for_tasks)
        self.points = points_for_tasks * successful_tasks
        self.points = self.points + (best_time - time) * point_for_error if  time<best_time and self.successful_tasks !=0 else self.points - (time - best_time) * point_for_error
        self.time = time

    def __str__(self):
        return f"{self.user_name}:{self.points}:{self.time}"


AMOUNT_TASK = 10
points_for_tasks = 1
USERS = ['Oleg', "katikovka", 'Vitaliy']

basic_tasks = []
for user in USERS:
    basic_tasks.append(Basic_Task(user, AMOUNT_TASK, random.randint(0, AMOUNT_TASK)))

basic_tasks.sort(key=lambda user: user.points, reverse=True)
print(*basic_tasks)


all_or_Nothing_tasks = []
for user in USERS:
    all_or_Nothing_tasks.append(All_or_Nothing(user, AMOUNT_TASK, random.randint(0, AMOUNT_TASK)))

all_or_Nothing_tasks.sort(key=lambda user: user.points, reverse=True)
print(*all_or_Nothing_tasks)

BEST_TIME = 8
POINT_FOR_ERROR = 1
fast_tasks = []
for user in USERS:
    fast_tasks.append(Fast(user,AMOUNT_TASK, random.randint(0, AMOUNT_TASK),  points_for_tasks,random.randint(0,10),BEST_TIME,POINT_FOR_ERROR))

fast_tasks.sort(key=lambda user: user.points, reverse=True)
print(*fast_tasks)