from functools import partial           # импорт для передачи параметров в кнопке
from tkinter import *                   # импорт модуля Tkinter
from tkinter.ttk import Combobox        # импорт класса Combobox для виджета
from tkinter.ttk import Radiobutton     # импорт класса для виджета кнопки
import tkinter as tk                    # импорт для Checkbutton
from tkinter import ttk, Label
import random as r                      # импорт для генератора чисел
from PIL import ImageTk, Image          # импорт для вставки изображений

result = 0
steps = {}
rad_list = []
rad1_check = None
rad1 = None
MONEY = 0
CASH = 0
PRICE = 0
label = None


def add_steps(key, val):
    steps[key] = val


def person():
    text_question.pack_forget()
    text.configure(text="Для начала создадим персонажа", font=("Arial Bold", 40))
    text_sex = Label(text="Кто ты?", font=("Arial Bold", 20))
    sex = Combobox(state="readonly")                                                    # создание выпадающего списка
    sex['values'] = ("Парень", "Девушка", "Вертолёт", "Олег Бабченок", "Колхозник (НЕТ)")
    text_name = Label(text="Имя", font=("Arial Bold", 20))
    input_name = Entry(width=20)                                                        # создание ячейки для ввода
    text_cash = Label(text="Введите любое число от 0 до 1042", font=("Arial Bold", 20))
    input_cash = Entry(width=20)

    text_sex.pack()
    sex.pack()
    text_name.pack()
    input_name.pack()
    text_cash.pack()
    input_cash.pack()
    text_question.pack()
    b.configure(text="Продолжить", font=("Arial Bold", 20), width=17, height=2,
                command=lambda: (mistake(input_name, text_cash, text_name, sex, text_sex, input_cash)))

    b.pack(side=BOTTOM)
    # sex.current(1)


def mistake(input_name, text_cash, text_name, sex, text_sex, inp_cash):
    try:
        inp = int(inp_cash.get())
        print(inp)
    except ValueError:
        text_question.configure(text="Введите, пожалуйста, число")
        text_question.pack()
        inp_cash.delete(0, END)
        b.configure(command=lambda: (mistake(input_name, text_cash, text_name, sex, text_sex, inp_cash)))
        b.pack(side=BOTTOM)

    else:
        global MONEY
        print("else")
        MONEY = inp
        inp_cash.pack_forget()
        text_cash.destroy()
        input_name.pack_forget()
        text_name.destroy()
        sex.destroy()
        text_sex.destroy()
        text_question.pack_forget()

        epilogue(input_name)


def epilogue(input_name):
    print(1)
    user_name = input_name.get()
    title.configure(text="Эпилог", font=("Arial Bold", 40))
    text.configure(text=f"""
        Привет, {user_name}. Вы стали новеньким в Колледже Сириус.
        Ваша группа 1.11.10.1 - кибербезопасность. Сегодня Ваш первый 
        день на занятиях, понедельник.
    
        Вы узнал всю необходимую информацию на канале колледжа, 
        нашли автобус и доехали до Арены. Дальше всё просто - 
        Вы шли за толпой и нашли аудиторию Шамони.
        Там было несколько свободных мест.
        Куда вы сядите?
        """,
                   font=("Arial Bold", 25), justify=LEFT)
    chose['values'] = ("К Игнату", "К Мише", "Сесть за свободную парту")
    chose.current(0)

    b.configure(text="Продолжить", command=partial(chose_desk, user_name, chose))

    title.pack(side=TOP)
    text.pack()
    chose.pack()


def chose_desk(user_name, chose):
    desk = {0: ignat,
            1: misha,
            2: free_desk}
    cur = (chose.current())
    chose.pack_forget()
    desk[cur](user_name)
    add_steps("lose", 0)


def ignat(user_name):
    steps["chose"] = 1
    title.configure(text="Первая пара")
    text.configure(text=
                   f"""
        Вы проходите на первую парту к Игнату. Первая пара Кулакова.
        Он заходит в аудиторию. Как обычно достаёт свой термо-стакан с кофе и черную 
        бутылку с неизвестной никому жидкостью.
        
        Кулаков: Всем привет, сегодня у нас с вами очередной нудный понедельник.
        
        Далее он объясняет новую тему.
        Все полтора часа вы слышали неизвестные вам термины и иногда смешные шутки.
        Пара подходит к концу. Начинается перерыв.
        """, font=("Arial Bold", 20), justify=LEFT)
    text_question.configure(text="Поговорить с Игнатом?")

    radioValue = tk.IntVar()
    rad1 = Radiobutton(menu, text='Поговорить', variable=radioValue, value=0)
    rad2 = Radiobutton(menu, text='Помолчать', variable=radioValue, value=1)
    b.configure(command=partial(talk_idnat, user_name, radioValue, rad1, rad2))

    text_question.pack()
    rad1.pack()
    rad2.pack()


def talk_idnat(user_name, radioValue, rad1, rad2):
    global label
    title.configure(text="Диалог с Игнатом")
    text_question.configure(text="")
    rad1.pack_forget()
    rad2.pack_forget()
    b.configure(command=partial(question_Anna))

    if radioValue.get() == 0:
        text.configure(text=f"""
        Вы: Привет
        Игнат: Привет
        Вы: Я {user_name}, тебя как?
        Игнат: Игнат, очень приятно. Как тебе тут?
        """)
        rad1 = Button(menu, text='Интересно, но ничего непонятно)', command=lambda i=None: (text.configure(
            text=text.cget("text") + "Вы: Интересно, но ничего непонятно)" + "\n        Игнат: Хах, это норма",
            font=("Arial Bold", 20), justify=LEFT), rad1.destroy(), rad2.destroy(), rad3.destroy()))
        rad2 = Button(menu, text='Мне нравится. Тут стульчики на колесиках.', command=lambda i=None: (
            text.configure(text=text.cget("text") + "Вы: Мне нравится. Тут стульчики на колесиках.\n        Игнат: ...",
                           font=("Arial Bold", 20), justify=LEFT), rad1.destroy(), rad2.destroy(), rad3.destroy()))
        rad3 = Button(menu, text='Скучно', command=lambda i=None: (
            text.configure(text=text.cget("text") + "Вы: Скучно\n        Игнат: Начнётся сессия, будет весело)",
                           font=("Arial Bold", 20), justify=LEFT), rad1.destroy(), rad2.destroy(), rad3.destroy()))
        rad1.pack()
        rad2.pack()
        rad3.pack()

    else:
        text.configure(text="*Молчание Егнят*")

        image = Image.open("/home/katikovka/Ignat.gif")
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(menu, image=photo)
        label.img = photo
        label.pack()
        b.configure(command=lambda: (label.destroy(), question_Anna()))


def question_Anna():
    title.configure(text="Вторая пара")
    text.configure(text="""
                            В аудиторию заходит преподаватель в черном выглаженном костюме
                            с кожаной сумочкой для ноутбука.
                            Его зовут Альберт...Андреевич.
                            
                            Пара началась с того, что два человека защищают доклад. 
                            Первая выходит Аня. После того, как она закончила, 
                            Альберт Андреевич спрашивает, есть ли у кого-то вопросы.
                            
                            """)
    text_question.configure(text="Задать вопрос Ане?")
    b.configure(text="Продолжить", command=partial(question_ignat))

    text_question.pack
    var1 = Button(menu, text="Да", command=lambda:
    (text.configure(text=text.cget("text") + "Аня как обычно придумала, что ответить."), var1.destroy(), var2.destroy()))
    var2 = Button(menu, text="Нет", command=lambda:
    (text.configure(text=text.cget("text") + "Вы не задави вопрос, Альбер думает, что Вы глупый."), var1.destroy(), var2.destroy()))
    text_question.pack()
    var1.pack()
    var2.pack()


def question_ignat():
    text.configure(text="""
                        После Ани выходит Игнат. Аналогично после своего выступления
                        ему задают вопросы по теме доклада.
                        
                    """)
    text_question.configure(text="Задать вопрос Игнату?")
    b.configure(command=partial(hall))
    var1 = Button(menu, text="Да", command=lambda:
        (text.configure(text=text.cget("text") + "     Игнат не смог ответить на этот вопрос.\n                         Он обиделся, вы больше не друзья"), var1.destroy(), var2.destroy(), add_steps("question", 1)))
    var2 = Button(menu, text="Нет", command=lambda:
        (text.configure(text=text.cget("text") + "Вы не задави вопрос, Альбер думает, что Вы глупый."), var1.destroy(), var2.destroy(), add_steps("question", 0)))
    text_question.pack()
    var1.pack()
    var2.pack()


def hall():
    if steps["chose"] == 1:
        if steps["question"] == 1:
            b.configure(command=partial(lose))
        else:
            b.configure(command=partial(dining))
    elif steps["chose"] == 2:
        b.configure(command=partial(dining))
    else:
        b.configure(command=partial(lose))


def lose():

    if steps["lose"] == 1:
        text.configure(text="""
                
                """)
        b.configure(command=partial(fin))
    else:
        text.configure(text="""
                    Дога в столовую - это очень нелегкий путь.
                    Так как Вы тут первый раз, не зная местности, Вы заблудились...
                    """)
        b.configure(command=partial(dining))
    text_question.configure(text="Куда идти?")
    b.pack_forget()

    var1 = Button(menu, text="Налево", command=lambda:
    (text.configure(text=text.cget("text") + "\nВы пошли налево..."),
     var1.configure(command=lambda:
     (text.configure(text=text.cget("text") + "\nВы пошли налево..."),
      (var1.pack_forget(), var4.configure(command=lambda:
      (text.configure(text=text.cget("text") + "\nВы заблудились."),
       add_steps("lose", 0), var4.pack_forget(), var2.pack_forget(), b.pack()))),
      var2.configure(command=lambda:
      (text.configure(text=text.cget("text") + "\nВы пошли направо..."),
       var1.pack_forget(),
       var3.configure(command=lambda:
       (text.configure(text=text.cget("text") + "\nВы пошли вперёд..."),
        var3.pack_forget(),
        var4.configure(command=lambda:
        (text.configure(text=text.cget("text") + "\nВы заблудились."), add_steps("lose", 0),
         var4.pack_forget(), var3.pack_forget(), var2.pack_forget(), b.pack()))))))))))

    var2 = Button(menu, text="Направо", command=lambda:
    (text.configure(text=text.cget("text") + "\nВы пошли направо..."),
     var2.pack_forget(), var3.configure(command=lambda:
    (text.configure(text=text.cget("text") + "\nВы пошли вперёд..."),
     var3.configure(command=lambda:
        (text.configure(text=text.cget("text") + "\nВы заблудились."), add_steps("lose", 0),
         var4.pack_forget(), var3.pack_forget(), var2.pack_forget(), b.pack()))))))

    var3 = Button(menu, text="Вперёд", command=lambda:
    (text.configure(text=text.cget("text") + "\nВы пошли вперёд..."),
     var3.configure(command=lambda:
     (text.configure(text=text.cget("text") + "\nВы пошли вперёд..."),
      var1.configure(command=lambda:
      (text.configure(text=text.cget("text") + "\nВы пошли налево..."),
       var1.pack_forget(),
       var2.configure(command=lambda:
       ((text.configure(text=text.cget("text") + "\nУРА ВЫ НЕ ЗАБЛУДИЛИСЬ!"),
        add_steps("lose", 1)),
        var2.pack_forget(),
        var3.pack_forget(),
        var4.pack_forget(),
        text_question.pack_forget(),
        b.pack()))))))))

    var4 = Button(menu, text="Назад", command=lambda i=None:
    (text.configure(text=text.cget("text") + "\nНазад нельзя, только вперёд!"),
     (var4.configure(command=lambda:
     (text.configure(text=text.cget("text") + "\nТак ты далеко не уйдёшь"),
      var4.configure(command=lambda:
      (text.configure(text=text.cget("text") + "\nБольше назад некуда"),
       var4.pack_forget())))))))

    var1.pack()
    var2.pack()
    var3.pack()
    var4.pack()


def dining():
    print(result)
    text_question.pack_forget()
    buy = Button(menu, text="Купить",
                 font=("Arial Bold", 20),
                 width=6,
                 height=1,
                 command=lambda: (cash_ost(cash_lbl, rad1)))
    cash_lbl = Label(menu, text=f"")
    amount = StringVar()
    amount_label = ttk.Label(textvariable=amount)
    price = ttk.Label()

    def select(rad1, PRICE):
        global result
        if rad1.get() == 1:
            result += PRICE
        elif rad1.get() == 0:
            result -= PRICE
        amount.set(result)

    def cash_ost(cash_lbl, rad1):
        global MONEY
        global PRICE
        CASH = MONEY - int(result)
        print(result)
        if (MONEY - int(result)) >= 0:
            buy.configure(text="Забрать", command=lambda: (text_question.configure(
                                                               text="Еда куплена. Теперь можно и покушать"),
                                                           [i.destroy() for i in rad_list],
                                                           cash_lbl.destroy(), price.destroy(), text_question.pack(), b.pack(), amount_label.destroy(), buy.destroy()))
            cash_lbl.configure(text=f"Осталось {CASH}")
        else:
            cash_lbl.configure(text=cash_lbl.cget("text") + f"\nНедостаточно средств")
            rad1_check.configure(variable=rad1, command=partial(select, rad1, PRICE))

            buy.configure(command=lambda: (cash_lbl.configure(text=f"На вашем счету: {MONEY}"), cash_ost(cash_lbl, rad1)))
            rad1_check.pack(**position)
            rad_list.append(rad1_check)
            buy.pack()

    b.pack_forget()
    title.configure(text="Столовая")

    text_question.configure(text="Что Вы купите?")
    position = {"padx": 6, "pady": 6, "anchor": NW}

    cash_lbl.configure(text=f"На вашем счету: {MONEY}")
    #cash_lbl.pack(**position)

    price_value = StringVar()
    price = ttk.Label(textvariable=price_value)
    #price.pack()

    def rad(TXT, PRICE):
        global rad1_check, price_value

        rad1 = IntVar()
        rad1_check = ttk.Checkbutton(text=TXT, variable=rad1, command=partial(select, rad1, PRICE))
        rad1_check.pack(**position)
        rad_list.append(rad1_check)
        return rad1

    #amount_label.pack(**position)

    def add_rad():
        rad("Салат Мужской каприз - 65 руб", 65)
        rad("Салат Ветерок - 45 руб", 45)
        rad("Паста Карбонара - 180 руб", 180)
        rad("Паста Фузилли с семгой и брокколи - 350 руб", 350)
        rad("Рис припущенный - 40 руб", 40)
        rad("Шашлык из свинины - 137 руб", 137)
        rad("Куриное филе с помидором и сыром - 150 руб", 150)
        rad("Суп Харчо с говядиной - 75 руб", 75)

    #buy.pack(**position)

    if steps["chose"] == 1:
        if steps["question"] == 1:
            if steps["lose"] == 1:
                text.configure(text=f"""
                        Наконец-то Вы дошли до столовой! Это было сложно.
                        Но Вы шли достаточно долго, из-за этого собралась уже очень большая очередь.

                        Время длится нереааааально долго...
                        
                        Но очередь всё таки заканчивается. Осталось очень мало времени до начала пары.
                        Нужно быстро выбрать, что поесть и спешить.
                        """, justify=LEFT)
                b.configure(command=lambda: (amount_label.pack_forget(), price.pack_forget(), lesson3()))
                cash_lbl.pack(**position)
                price.pack()
                amount_label.pack(**position)
                add_rad()
                buy.pack(**position)

            else:
                text.configure(text=f"""
                    Вы очень долго ходили по коридорам и не смогли найти столовую.
                    Да и времени кушать уже нет, до пары осталось мало времени, нужно идти обратно.
                    
                    *желудок грустно урчит*
                    """)
                add_steps("home", 1)
                b.configure(command=lesson3)
                b.pack()
        else:
            text.configure(text=f"""
                    После второй пары больой перерыв на обед. 
                    Игнат Вас познакомил с Виталей и Никитой, и вы вместе пошли в столовую.
                    Когда вы стали в очередь, к вам подошли ещё несколько друзей, 
                    и Вы со всеми познакомились. 
                    Теперь Вы знакомы с программистами и сисадминами. Возможно. Вам это пригодится.
                    
                    Вы не замечаете, как быстро очередь подходит. И теперь пришло время очень сложного выбора.
                                """)
            b.configure(command=lambda: (amount_label.pack_forget(), price.pack_forget(), lesson3()))
            cash_lbl.pack(**position)
            price.pack()
            amount_label.pack(**position)
            add_rad()
            buy.pack(**position)

    elif steps['chose'] == 2:
        text.configure(text=f"""
            После второй пары начинается обед.
            Миша помог Вам без проишествий дойти до столовой.
            Тут как обычно очередь в 6578345678км, поэтому вы много болтаете.
            
            Миша:Ты еще не знаешь, но Дмитрий Владимирович дал нам ДЗ.
            Необходимо на Убунте установить Аманду и разобраться с ней.
            Вы:Что это такое?
            Миша:Тебе повезло, что я уже разобрался.
            ...
            И дальше скучнейший разговор про Аманду.
            """)
        b.configure(command=lambda: (amount_label.pack_forget(), price.pack_forget(), lesson3()))
        cash_lbl.pack(**position)
        price.pack()
        amount_label.pack(**position)
        add_rad()
        buy.pack(**position)

    elif steps['chose'] == 3:
        if steps.get('lose') == 1:
            text.configure(text=f"""
                        Наконец-то Вы дошли до столовой! Это было сложно.
                        Но Вам повезло, что достаточно быстро нашли дорогу.
                        Поэтому очередь не такая большая.
                        
                        Теперь выберите, что хотите поесть:
                """)
            b.configure(command=lambda: (amount_label.pack_forget(), price.pack_forget(), lesson3()))
            cash_lbl.pack(**position)
            price.pack()
            amount_label.pack(**position)
            add_rad()
            buy.pack(**position)
        else:
            text.configure(text=f"""
                Вы очень долго блуждали по коридорам, а перерыв не бесконечный.
                
                Пара уже началась, с трудом Вы добрались обратно в кабинет.
                """)
            b.configure(command=lesson3)
            b.pack()

    text.pack()


def new_friend():
    if steps["question"] == 0:
        text.configure(text="""
            Вы садитель за стл с Игнатом. Он предлагает посвятить Вас в колхозники.
            
            P.c. Вообще настоящий Игнат сказал, что без ангара никак, но Вас мы всё таки посвятим.
            
            Игнат: Итак, чтобы тебе стать настоящим колхозником, нам понадобятся вилы.
                   Нам очень повезло, что мы находимся в столовой. Тебе понадобится вилка.
                   А теперь, самая сложная задача, я надеюсь, ты с ней справишься:
                   Тебе нужно сьесть всю еду одной вилкой.
                   Именно так появился первый колхозник.            
            """)
        text_question.configure(text="Выполнить указания Игната?")
        b.configure(command=partial(lesson3))
        rad1 = Button(menu, text='Да', command=lambda: (
            text.configure(text="ПОЗДРАВЛЯЕМ, ТЕПЕРЬ ВЫ СТАЛИ КОЛХОЗНИКОМ!\n\nP.s.Можно поаплодировать"),
            rad1.pack_forget(), rad2.pack_forget(), text_question.pack_forget()))
        rad2 = Button(menu, text='Неее', command=lambda: (
            text.configure(text="Вы отказались. Игнат и все остальные с презрением на Вас смотрят"), rad1.pack_forget(),
            rad2.pack_forget(), text_question.pack_forget()))

        text.pack()
        text_question.pack()
        rad1.pack()
        rad2.pack()
        b.pack(side=BOTTOM)
    else:
        text.configure(text="""
            Вы ели в одиночестве.
            """)

    b.configure(command=lambda: (lesson3()))
    text.pack()
    b.pack(side=BOTTOM)


def lesson3():
    text_question.pack_forget()
    title.configure(text="""Третья пара

                    Её ведёт мужчина, все называют его Торшин.
                    Он постоянно настораживающе смеется.""")
    if steps["chose"] == 1:
        if steps["question"] == 1:
            if steps["lose"] == 1:
                text.configure(text="""
                                       Вы вернулись после обеда, и по прежнему сели к Игнату.
                                       Он всё ещё обижен, поэтомк не обращает на Вас внимания.

                                       Торшин спрашивает про какую-то Аманду, но Вы ничего не знаете.
                                       А Игнат не отвечает.

                                       Вы слушаете и пытаетесь что-то понять.""")
            elif steps["lose"] == 2:
                text.configure(text="""
                                       Вы с возвращаетесь на пару. Игнат всё ещё обижен на Вас, 
                                       поэтому Вы садитесь за свободную парту.

                                       Торшин спрашивает про какую-то Аманду, но Вы ничего не понимаете.
                                       Поэтому вы сидите и разговариваете со своим урчащим желудком.""")
        else:
            text.configure(text="""
                        Вы сидите с Игнатом, но это особо Вас не спасает.
                        Торшин спрашивает про какую-то Аманду.
                        Игнат сам не сильно разобрался в Аманде, поэтому вы вдвоём сидите молча.
                        """)

    elif steps["chose"] == 2:
        text.configure(text="""
                       Вам очень повезло, что Вы сидите с Мишей!

                       Торшин спрашивает про какую-то Аманду, а вы сидите с единственным человеком, 
                       который отлично знает, что это такое.
                       Втечение пары он Вам всё объяснял и даже помог установить!
                                """)
    elif steps["chose"] == 3:
        if steps["lose"] == 1:
            text.configure(text="""
                                Вы возвращаетесь со столовой и садитесь за свою парту.
                                Торшин спрашивает про какую-то Аманду. Вам ничего не понятно.
                                Ну просто от слова СОВСЕМ.
                                О чём они вообще говорят?
                                """)
        else:
            text.configure(text="""
                                Аккуратно открываете дверь, преподаватель уже там.

                                Когда вы зашли, он Вас заметил и обратил внимание.
                                И тут же зада вопрос про какую-то Аманду.
                                Вы просто расстерянно стояли и даже не понимали, о чём он говорил.
                                Торщин понял, что Вы ничего не знаете, и оставил впокое.

                                Всю оствшуюся пару Вы слушали и начали понимать, что такое Аманда.
                                Перелазили кучу сайтов и нашли информацию.
                                """)
    title.pack()
    b.configure(command=home)


def home():
    b.pack_forget()
    title.configure(text="Пора домой!")
    if steps["chose"] == 1:
        if steps["question"] == 1:
            chose['values'] = ("Пойти пешком", "Поехать на автобусе", "Поехать на такси")
            chose.current(0)
            text.configure(text="""
            Пары закончились, и теперь нужно выбрать, как добраться домой.
            """)
            c = Button(menu, text="Выбрать",
                       font=("Arial Bold", 20),
                       width=10,
                       height=2,
                       command=lambda: (c.pack_forget(), chose_way(chose)))
            chose.pack()
            c.pack()
        else:
            text.configure(text="""
            Ещё до конца третьей пары Игнат заказал такси.
            Он любезно позвал Вас поехать вместе.
                    """)
            b.configure(command=fin)
            b.pack(side=BOTTOM)
    elif steps["chose"] == 2:
        text.configure(text="""
        Миша предложил Вам пойти пешком.
        Он показал Вам дорогу и по пути рассказал ещё много полезного.
                            """)
        b.configure(command=fin)
        b.pack(side=BOTTOM)
    elif steps["chose"] == 3:
        chose['values'] = ("Пойти пешком", "Поехать на автобусе", "Поехать на такси")
        chose.current(0)
        text.configure(text="""
                Пары закончились, и теперь нужно выбрать, как добраться домой.
                    """)
        c = Button(menu, text="Выбрать",
                   font=("Arial Bold", 20),
                   width=10,
                   height=2,
                   command=lambda: (c.pack_forget(), chose_way(chose)))
        chose.pack()
        c.pack()


def cost():
    global CASH
    cash_lbl = Label(menu, text=f"")
    if (CASH - MONEY) >= 0:
        cash_lbl.configure(text=f"На вашем счету {CASH}")
        b.configure(text="Поехали!", command=lambda: (chose.pack_forget(), fin()))
        steps["cost"] = 1
        # b.pack(side=BOTTOM)
    else:
        cash_lbl.configure(text=f"На вашем счету {CASH}")
        cash_lbl.configure(text=f"Недостаточно средств")
        b.configure(command=lambda: (chose.pack_forget(), cash_lbl.pack_forget(), foot()))
        cash_lbl.pack()


def chose_way(chose):
    way = {0: foot,
           1: bus,
           2: taxi}
    way[chose.current()](chose)


def foot(chose):
    add_steps("home", 1)
    chose.pack_forget()
    steps["way"] = 1
    text.configure(text="""
        Вы отправляетесь домой пешком. В Сириусе Вы ни разу не были,
        и не знаете, куда идти.
        Вам предстоит сложная дорога.
        
        Удачи не заблудиться!
        """)
    b.configure(command=lose)


def bus(chose):
    chose.pack_forget()
    steps["way"] = 2
    global MONEY
    MONEY = 30

    text.configure(text=f"""
        Вы отправляетесь домой на автобусе.
        Вас можно назвать по истине бестрашным!
        Потому что только самые отчаянные выберут ехать на автобусе.
        
        Проезд стоит 30 руб.1
        """)
    b.configure(command=fin)
    b.pack(side=BOTTOM)


def taxi(chose):
    steps["way"] = 3
    MONEY = r.randint(100, 301)
    chose.pack_forget()
    text.configure(text=f"""
        Вы отправляетесь домой нa такси.
        Интересно, какие там цены сейчас?...
        
        Итак, такси стоит {MONEY} руб.
        """)
    b.configure(command=fin)
    b.pack(side=BOTTOM)


def fin():
    if steps["chose"] == 1:
        text.configure(text="""
                    У меня есть для Вас две новости!
                    
                    Первая - хорошая. Вы сумели добраться домой!
                    Вторая - плохая. Вы попали в матрицу времени и не прошли игру.    
                    Подумайте, что вы делаете не так.
                    """)
        b.configure(text="Начать заново", command=lambda: (title.configure(text=""), text_question.pack_forget(), person()))
    elif steps["chose"] == 2:
        title.configure(text="!!!Пздравляю!!!")
        text.configure(text=""" 
                Вы прошли игру и всё делали правильно.
                    
                Только так можно выжить в колледже Сииус.
                Вы правильно сделали, что выбрали сесть к Мише, 
                узнали много нового и дальше Вас точно не отчислят! (надейся)
                        """)
        b.configure(text="Ёмае, а он крут!", command=photo)
    elif steps["chose"] == 3:
        text.configure(text="""
                У меня есть для Вас две новости!

                Первая - хорошая. Вы сумели добраться домой!
                Вторая - плохая. Вы попали в матрицу времени и не прошли игру.    
                Подумайте, что вы делаете не так.
                            """)
        b.configure(text="Начать заново", command=lambda: (title.configure(text=""), text_question.pack_forget(), person()))


def photo():
    text.pack_forget()
    image = Image.open("/home/katikovka/fin.gif")
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(menu, image=photo)
    label.img = photo
    label.pack()


def misha(user_name):
    steps["chose"] = 2
    title.configure(text="Первая пара")
    text.configure(text=
                   f"""
                {user_name}, ты проходишь на первую парту к Мише. Первая пара Кулакова.
                
                Он заходит в аудиторию. Как обычно достаёт свой термо-стакан с кофе и черную 
                бутылку с неизвестной никому жидкостью.
                
                Кулаков: 'Всем привет, сегодня у нас с вами очередной нудный понедельник.'
                
                Далее он объясняет новую тему.
                Все полтора часа вы болтали с Мишей. Хорошо познакомились и даже немного
                подружились.
                Начинается перерыв.
                """, font=("Arial Bold", 20), justify=LEFT)
    b.configure(text="Ёмае, а он крут", command=partial(rest))


def rest():
    title.configure(text="Перерыв")
    text.configure(text=f"""
                Никакого вам перерыва, вы слушаете байки преподавателя дальше.
                Итого: пара длится 105 минут (если не больше)
                """, font=("Arial Bold", 20), justify=LEFT)
    b.configure(text="Продолжить", command=partial(question_Anna))


def luck():
    title.configure(text="Третья пара")
    text.configure(text=
                   f"""
    Вы выжили!
                            """, font=("Arial Bold", 20), justify=LEFT)
    b.configure(command=partial(end))


def end():
    title.configure(text="Пора домой!")
    text.configure(text=f"""
            Пары кончились, пора идти домой.
            Миша почти всегда ходит пешком, так что и вы тоже пойдете.
            Удачи!
            """, font=("Arial Bold", 20), justify=LEFT)


def free_desk(user_name):
    steps["chose"] = 3
    title.configure(text="Первая пара")
    text.configure(text=f"""
            {user_name}, ты проходишь к свободной парте и садишься. Первая пара Кулакова.
            Он заходит в аудиторию. Как обычно достаёт свой термо-стакан с кофе и черную 
            бутылку с неизвестной никому жидкостью.
                
            Кулаков: Всем привет, сегодня у нас с вами очередной нудный понедельник.
            *Далее мы наблюдаем как какой-то дядя с хвостиком и сережкой в ухе раскладывает 
            свои 56798274892 слайдов.*""", font=("Arial Bold", 20), justify=LEFT)
    b.configure(command=partial(sleeping))


def sleeping():
    text.configure(text=f"""
        К сожалению, преподаватель говорит очень тихо и Вас клонит в сон...""",
                   font=("Arial Bold", 20), justify=LEFT)
    radioValue = tk.IntVar()
    rad1 = Radiobutton(menu, text='Не буду спать! Слишком нужная пара',
                       variable=radioValue, value=0)
    rad2 = Radiobutton(menu, text='Ничего страшного не произойдет, если я немного подремаю',
                       variable=radioValue, value=1)
    rad1.pack()
    rad2.pack()
    b.configure(text="Продолжить", command=partial(sleep, rad1, rad2, radioValue))


def sleep(rad1, rad2, radioValue):
    title.configure(text="Первая пара")
    rad1.pack_forget()
    rad2.pack_forget()
    if radioValue.get() == 0:
        text.configure(text=f"""
        Поздравляю! 
        
        Теперь вы полтора часа будете слушать кучу баек 
        вперемешку с непонятными терминами!""")
        b.configure(command=partial(question_Anna))
    elif radioValue.get() == 1:

        text.configure(text=f"""
        Поздравляю! Вы вступили в клуб спящих на паре!

        К сожалению, так делать нельзя и Вам придется написать объяснительную.""")
        b.configure(text="Грустно :(", command=partial(talkToRenata))


def talkToRenata():
    text.configure(text=f"""
            Пара кончилась, Вас разбудила Рената:
            -Хей, вставай!""")
    radioValue = tk.IntVar()
    rad1 = Radiobutton(menu, text='Я еще немножко, мааам...',
                       variable=radioValue, value=0)
    rad2 = Radiobutton(menu, text='Да, встаю.',
                       variable=radioValue, value=1)
    b.configure(text="Продолжить", command=partial(albert, rad1, rad2))
    rad1.pack()
    rad2.pack()


def albert(rad1, rad2):
    rad1.pack_forget()
    rad2.pack_forget()
    text.configure(text=f"""
            Просыпайся, сейчас пара Альберта Андреевича.
            Если он Вас увидит спящим, заставит еще одну объяснительную писать.""")
    b.configure(text="Встаю", command=question_Anna)


menu = Tk()                             # создание окна
menu.title("Новенький")                 # текст в шапке окна
menu.geometry("1900x900")               # размер окна
title = Label(menu, text="")            # создание текста
text_question = Label(menu, text="",
                      font=("Arial Bold", 30))
text = Label(menu, text="Добро пожаловать\nв игру симулятор 'Новенький'",
             font=("Arial Bold", 40))   # создание текста в окне
chose = Combobox(menu, width=25)
input_cash = Entry(width=20)
input_cash.pack_forget()

b = Button(menu, text="Начать",
           font=("Arial Bold", 30),
           width=15,
           height=2,
           command=person)              # заднание кнопки с текстом

title.pack()                            # расположение объектов
text.pack()
b.pack()
menu.mainloop()                         # запуск окна
