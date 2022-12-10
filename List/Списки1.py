games = []
while True:
    game = input("Введите название настолькой игры: ")
    if game != "0":
        if game not in games:
            games.append(game)
            games.sort()
            print("Игра добавлена в список")
        else:
            print(("Эта игра уже записана"))
    else:
        break


