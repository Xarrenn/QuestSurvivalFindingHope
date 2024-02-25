import time
from funks import universal, ends
from texts import chapter_2_text

print(chapter_2_text.logo())
print(31*' ',end='')
universal.slow_text("Глава вторая: первые шаги к разгадке \n\n", _time=0.09)
time.sleep(2)
universal.slow_text(chapter_2_text.history())
input("Нажмите Enter чтобы осмотреться")
universal.slow_text(chapter_2_text.look_around())

current_room = "Зал"
find_out = False
key = False
food = False
open_door = False
dct = {"консерва": False}

while not open_door:
    if current_room == "Зал":
        universal.slow_text("Я Нахожусь в главном зале:\n")
        time.sleep(0.5)
        print("[1] Пройти в подсобку.\n"
              "[2] Заглянуть за прилавок.\n"
              "[3] Пройти по коридору.\n",)
        while True:
            try:
                where = int(input("Выбери действие: "))
                if where < 1 or where > 3:
                    print("введите число от 1 до 3")
                else:
                    break
            except ValueError:
                print("введите ЧИСЛО от 1 до 3")
        if where == 1:
            current_room = "Подсобка"
            universal.slow_text(chapter_2_text.utility_room())
        elif where == 2:
            current_room = "Прилавок"
            universal.slow_text(chapter_2_text.counter())
        else:
            current_room = "Кладовая"
            if not food:
                universal.slow_text(chapter_2_text.stock())
            else:
                universal.slow_text(chapter_2_text.stock_2())

    elif current_room == "Подсобка":
        universal.slow_text("Я Нахожусь в подсобке:\n")
        print("[1] Осмотреть коробку.\n"
              "[2] Вернуться в зал.\n")
        while True:
            try:
                where = int(input("Выбери действие: \n"))
                if where < 1 or where > 2:
                    print("введите число 1 или 2")
                else:
                    break
            except ValueError:
                print("введите ЧИСЛО 1 или 2")
        if where == 1:
            if not key:
                universal.slow_text(chapter_2_text.box())
                key = "Спасение"
                if not find_out:
                    universal.slow_text("-У меня есть пароль но от чего он.\n\n")
                else:
                    universal.slow_text("Похоже этот пароль от той двери на складе.\n\n")
            else:
                universal.slow_text("Я уже осмотрел коробку.\n")
            current_room = "Подсобка"
        elif where == 2:
            current_room = "Зал"

    elif current_room == "Прилавок":
        universal.slow_text("Я Нахожусь за прилавком:\n")
        print("[1] Осмотреться.\n"
              "[2] Вернуться в зал.\n")
        while True:
            try:
                where = int(input("Выбери действие: \n"))
                if where < 1 or where > 3:
                    print("введите число 1 или 2")
                else:
                    break
            except ValueError:
                print("введите ЧИСЛО 1 или 2")
        if where == 1:
            universal.slow_text("*-Здесь только засохшие куски заплесневевшего хлеба*. С грустью в голосе сказали вы.\n")
            current_room = "Прилавок"
        elif where == 2:
            current_room = "Зал"

    elif current_room == "Кладовая":
        universal.slow_text("Я на складе:\n")
        print("[1] Осмотерть стеллажи.\n"
              "[2] Вернуться в зал.")
        if dct["консерва"]:
            print("[3] Перекусить.")
        if find_out:
            print("[4] Проверить что за дверью.\n")
        while True:
            try:
                where = int(input("Выбери действие: \n"))
                if where < 1 or where > 4:
                    print("введите число из перечисленных:")
                else:
                    break
            except ValueError:
                print("введите ЧИСЛО из перечисленных:")

        if where == 1:
            if not food and not find_out:
                universal.slow_text(chapter_2_text.food())
                dct["консерва"] = True
                food = True
                current_room = "Кладовая"
            elif food and not find_out:
                universal.slow_text(chapter_2_text.second_check())
                find_out = True
                current_room = "Кладовая"
            else:
                universal.slow_text("Думаю я уже все здесь осмотрел.\n")
                current_room = "Кладовая"
        elif where == 2:
            current_room = "Зал"
        elif where == 3:
            universal.slow_text("Вы скушали консерву немного насытившись.\n")
            dct["консерва"] = False
            current_room = "Кладовая"
        elif where == 4:
            universal.slow_text(chapter_2_text.secret_door())
            current_room = "Дверь в подвал"

    elif current_room == "Дверь в подвал":
        universal.slow_text("Я у двери в подвал. \n\n")
        if key:
            print("[1] Ввести пароль.\n"
                  "[2] Вернуться.\n")
        else:
            print("-Нужно найти пароль.\n"
                  "[1] Вернуться.\n")
        while True:
            try:
                where = int(input("Выбери действие: \n"))
                if where < 1 or where > 2:
                    print("введите число из перечисленных:")
                else:
                    break
            except ValueError:
                print("введите ЧИСЛО из перечисленных:")
        if where == 1 and key:
            password = input("Пароль: \n")
            if password == key:
                universal.slow_text(chapter_2_text.open_door())
                open_door = True
            else:
                print("Неправильный пароль.")
                current_room = "Дверь в подвал"
        elif where == 1:
            current_room = "Кладовая"
time.sleep(3)
print(chapter_2_text.logo())
print(36*' ',end='')
universal.slow_text("Продолжение следует.... \n\n", _time=0.09)
print('\n'*30)







