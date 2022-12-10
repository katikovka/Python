from datetime import *


def analyzer():
    req = input(("__________________________________\nВведите любой запрос, связанный с расписанием, временем, друзьями или котиками:\n__________________________________\n"))
    while True:
        if "расп" in req.lower():
            schedule()
        elif "кот" in req.lower() or "кош" in req.lower():
            cat()
        elif "врем" in req.lower() or "час" in req.lower():
            time()
        elif "дру" in req.lower():
            chek_friends()
        else:
            print("\_(ツ)_/¯\nТакого запроса нет, или он не распознан.\nПопробуйте ещё раз.")
            analyzer()


def schedule():
    day = input("Введите день недели:\nНАЗАД - чтобы выйти\n")
    if "на" in day.lower():
        analyzer()
    if "пн" in day.lower() or "пон" in day.lower():
        print("Расписание на ПОНЕДЕЛЬНИК:\n 1. ИБ\n 2. ЭИТСС\n 3. ИТ\n")
    elif "вт" in day.lower():
        print("Расписание на ВТОРНИК:\n 1. Физ-ра\n 2. Python\n 3. Английский\n 4. Архитектура ВТ")
    elif "ср" in day.lower():
        print("Расписание на СРЕДУ:\n 1. СУБД\n 2. Вышмат\n 3. Вышмат\n 4. Python")
    elif "ч" in day.lower():
        print("Расписание на ЧЕТВЕРГ:\n 1. Алгоритмы\n 2. История\n 3. ПиПАСЗИ\n 4. Сети")
    elif "пт" in day.lower():
        print("Расписание на ПЯТНИЦУ:\n 1. Python\n 2. Алгоритмы\n")
    elif "су" in day.lower() or "сб" in day.lower():
        print("Расписание на СУББОТУ:\n 1. Архитектура ВТ\n 2. Английский\n")
    elif "вс" in day.lower() or "вос" in day.lower():
        print("""В ВОСКРЕСЕНЬЕ выходной!
                   __..--''``---....___   _..._    __
 /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
///_.-' _..--.'_    \                    `( ) ) // //
/ (_..-' // (< _     ;_..__               ; `' / ///
 / // // //  `-._,_)' // / ``--...____..-' /// / //
        """)
    else:
        print("\_(ツ)_/¯\nТакого запроса нет, или он не распознан.\nПопробуйте ещё раз.")


def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    print("ヾ(⌐■_■)ノ♪\nВы нашли бонусный запрос!\n")
    return bonus_time()


def bonus_time():
    value = input("Хотите узнать, сколько осталось до сессии?\nДа/Нет\n")
    if "д" in value.lower():
        now = datetime.today()
        day_x = datetime(2022, 12, 19)
        d = day_x - now  # str(d)  '83 days, 2:43:10.517807'
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        print('До сессии осталось: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
        return analyzer()
    elif "н" in value.lower():
        return analyzer()
    else:
        print("(ಠ_ಠ)\nНе совсем понял твоего ответа.\n")
        return bonus_time()


def friends(friend):
    value = (input("Выберите:\n 1. Добавить друга.\n 2. Удалить друга.\n 3. Посмотреть список друзей.\n 4. Задать другойи запрос.\n"))
    if value == "1":
        person = input("Введите имя и фамилию:\n")
        friend.append(person)
        print("Друг добавлен.\n")
        print(friend)
    elif value == "2":
        if friend:
            print(friend)
            while True:
                index = input("Введите номер друга, которого нужно удалить:\n")
                if int(index) > 0 and (int(index)-1) <= len(friend):
                    index = int(index) - 1
                    friend.pop(index)
                    print("Ваш список друзей:\n", friend)
                    break
                else:
                    print("Такого номера нет.")
        else:
            return chek_friends()
    elif value == "3":
        print("Ваш список друзей:\n", friend)
    elif value == "4":
        return analyzer()
    else:
        print("\_(ツ)_/¯\nТакого запроса нет, или он не распознан.\nПопробуйте ещё раз.\n")


def chek_friends():
    friend = []
    while True:
        if friend:
            friends(friend)
        else:
            print("Пока у тебя нет друзей")
            friends(friend)


def cat():
    pic1 = """
    ..........／＞　 フ............
    　　　　　| 　_　 _|
    　 　　　／`ミ _x 彡
    　　 　 /　　　 　 |
    　　　 /　 ヽ　　 ﾉ
    　／￣|　　 |　|　|
    　| (￣ヽ＿_ヽ_)_)
    　＼二つ
    """
    pic2 = """
      ,-.       _,---._ __  / \\
     /  )    .-'       `./ /   \\
    (  (   ,'            `/    /|
     \  `-"             \\'\   / |
      `.              ,  \ \ /  |
       /`.          ,'-`----Y   |
      (            ;        |   '
      |  ,-.    ,-'         |  /
      |  | (   |        hjw | /
      )  |  \  `.___________|/
      `--'   `--'
    """
    pic3 = """
                                                   .--.
                                                   `.  \\
                                                     \  \\
                                                      .  \\
                                                      :   .
                                                      |    .
                                                      |    :
                                                      |    |
      ..._  ___                                       |    |
     `."".`''''""--..___                              |    |
     ,-\  \             ""-...__         _____________/    |
     / ` " '                    `""""""""                  .
     \                                                      L
     (>                                                      \\
    /                                                         \\
    \_    ___..---.                                            L
      `--'         '.                                           \\
                     .                                           \_
                    _/`.                                           `.._
                 .'     -.                                             `.
                /     __.-Y     /''''''-...___,...--------.._            |
               /   _."    |    /                ' .      \   '---..._    |
              /   /      /    /                _,. '    ,/           |   |
              \_,'     _.'   /              /''     _,-'            _|   |
                      '     /               `-----''               /     |
                      `...-'                                       `...-'
    """

    req = input("Какого котика вывести?\n  1. Грусный котик.\n  2. Котик в коробке.\n  3. Большой котик.\n  4. Выйти.\n")

    if req == "1":
        print(pic1, "\n________________________________________________________________\n")
    elif req == "2":
        print(pic2, "\n________________________________________________________________\n")
    elif req == "3":
        print(pic3, "\n________________________________________________________________\n")
    elif req == "4":
        return analyzer()
    else:
        print("\_(ツ)_/¯\nТакого запроса нет, или он не распознан.\nПопробуйте ещё раз.\n")