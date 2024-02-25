import sys
import time
from random import randint
from funks import universal, ends
from texts import chapter_1_text
dct={"бинт": False}
#print(dct["пластырь"])                #вывод по ключу
#dct["пластырь"] = "шляпа"             #замена ключа
#print(dct)                            #все выводит
#dct["что-то"]                         #проверяет что-то если тру то делает


print(chapter_1_text.second_history())
print(34*' ',end='')
universal.slow_text("Глава первая: Пробуждение \n\n", _time=0.09)
universal.slow_text(chapter_1_text.third_history())

a = int(input("напиши,[1] чтобы внимательнее осмотреть комнату\n"))
while a != 1:
    a = int(input())
    if a == 1:
        break

if a == 1:
    universal.slow_text(chapter_1_text.Inspect_room())

print("Действия:\n"
      "[1] Посмотреть в окно.\n"
      "[2] зайти в ванную.\n"
      "[3] Осмотреть шкаф.\n"
      "[4][выход] Выйти из комнаты.\n")

var = 1
while var:
    try:
        var = int(input('Напиши число действия: '))
    except ValueError as e:
        print('Введи число.')
    match var:
        case 1:
            universal.slow_text(chapter_1_text.look_out_window())
        case 2:
            universal.slow_text(chapter_1_text.door_bathroom())
            dct["бинт"]=True
        case 3:
            universal.slow_text(chapter_1_text.closet())
        case 4:
            universal.slow_text(chapter_1_text.exit())
            break

random_number = 4
flag = False
for i in range(0, 3):
    try:
        choice = int(input('Введи число с замка: \n'))
        if choice == random_number and i == 0:
            flag = True
            universal.slow_text("*получилось дверь открылась*\n")
            break
        elif choice == random_number and i > 0:
            universal.slow_text("*получилось дверь потдалась нужно делать ноги пока они не пробились!*\n")
            break
    except ValueError:
        universal.slow_text("\n-блять тут не букв\n")
    if i == 0:
        universal.slow_text("-Черт похоже здесь стоит сигнализация\n"
                            "*ты оглядываешься и видешь приблежабщиеся силуэты за окном и приглушоный рык *\n")
    elif i == 1:
        universal.slow_text("-Вот Б***ь, они ломятся в окно с**а, нужно срочно угадать число, соберить!\n")
    elif i == 2:
        universal.slow_text("*ходячии трупы пробили окно и вкусно перекусили твоей вскусненькой плотью*\n")
        universal.slow_text(ends.first_end())
        sys.exit(1)

if flag:
    universal.slow_text(chapter_1_text.pered_quiet_exit())
    input("Нажмите Enter чтобы продолжить")
    universal.slow_text(chapter_1_text.quiet_exit())


    (input("напиши ,[1] чтобы прочитать что написанно на газетке.\n"))
    universal.slow_text(chapter_1_text.newspaper())
    input("Нажмите Enter чтобы продолжить")
    universal.slow_text(chapter_1_text.telegram())
    input("Нажмите Enter чтобы продолжить\n")

    print("Действия:\n"
          "[1] сходить до пекарни по указателю.\n"
          "[2] осмотреть дома поблизости в поисках еды.\n")

    while True:
        try:
            var = int(input('Напиши число действия: \n'))
        except ValueError as e:
            print('Введи число.')
        match var:
            case 1:
                universal.slow_text(chapter_1_text.bakery())
                break
            case 2:
                universal.slow_text(chapter_1_text.home())

    print("Действия:\n"
          "[1] идти напрямую.\n"
          "[2] пройти незаметно.\n"
          "[3] подойти к парочке и спросить что происходит.\n")

    var = 10
    while var:
        try:
            var = int(input('Напиши число действия: \n'))
        except ValueError as e:
            print('Введи число.')
        match var:
            case 1:
                universal.slow_text(chapter_1_text.directly())
                random_number = randint(1, 2)
                choice = int(input('Введи число [1-2]: \n'))
                if choice == random_number:
                    print("*вы попали внутрь*\n")
                else:
                    print("*вы попали внутрь но повредили руку*\n")
                universal.slow_text("*пока вы шли как король и справлялись с дверью та парочка направилась в вашу сторону*\n\n")
                break
            case 2:
                universal.slow_text(chapter_1_text.carefully())
                break
            case 3:
                universal.slow_text(chapter_1_text.Strangers())
                time.sleep(5)
                universal.slow_text(ends.first_end_2())
                sys.exit(1)


elif flag==False:
        input("Нажмите Enter чтобы продолжить\n")
        universal.slow_text(chapter_1_text.dangerous_exit())
        print("Действия:\n"
              "[1] бегло оглядется осмотреться.\n"
              "[2] наорать на них чтоб не подходили\n"
              "[3] попробовать закрыть дверь\n"                              #сделать сисетму времени дается примерно 10 сек 
              "[4] бежать в неизваевстном направлении.\n")                   #каждый вариант забирает время если не успел 1 концовка смерть
        var = 1
        while var:
            try:
                var = int(input('Напиши число действия: \n'))
            except ValueError as e:
                print('Введи число.')
            match var:
                case 1:
                    universal.slow_text(chapter_1_text.quick_look_around())
                    var2=1
                    break
                case 2:
                    universal.slow_text(chapter_1_text.scream())
                case 3:
                    universal.slow_text(chapter_1_text.close_the_door())
                case 4:
                    universal.slow_text(chapter_1_text.run_away())
                    time.sleep(5)
                    universal.slow_text(ends.first_end_3())
                    sys.exit(1)

        print("Действия:\n"
              "[1] залезть на дерево.\n"
              "[2] спрятаться под столом.\n"
              "[3] бежать вверх по дороге.\n")
        var2 = 10
        while var2:
            try:
                var2 = int(input('Напиши число действия: \n'))
            except ValueError as e:
                print('Введи число.')
            match var2:
                case 1:
                    universal.slow_text(chapter_1_text.climb_a_tree())
                    time.sleep(5)
                    universal.slow_text(ends.first_end_3())
                    break
                case 2:
                    universal.slow_text(chapter_1_text.table())
                case 3:
                    universal.slow_text(chapter_1_text.run_the_road())
                    break

        input("Нажмите Enter чтобы продолжить\n")
        universal.slow_text(chapter_1_text.run_the_bakery())
        input("Нажмите Enter чтобы продолжить\n")
        universal.slow_text(chapter_1_text.run_the_bakery_2())
        universal.slow_text("Подбегая ближе к зданю вы замечаете что главная дверь зставлена барикадами\n")

        print("Ваши действия:\n"
              "[1] бежать на пролом\n"
              "[2] бежать на задний двор\n")
        var = 1
        while var:
            try:
                var = int(input('Напиши число действия: \n'))
            except ValueError as e:
                print('Введи число.')
            if var == 1:
                universal.slow_text(chapter_1_text.punch_forward())
                var2 = 1
                break
            else:
                universal.slow_text(chapter_1_text.behind_bakery())
                break

        if var == 1:
            print("Что делать?:\n"
                  "[1] использовать бинт\n"
                  "[2] толкнуть телом с разбега\n"
                  "[3] пнуть ногой\n")
            while True:
                try:
                    var2 = int(input('Напиши число действия: \n'))
                except ValueError as e:
                    print('Введи число.')
                if var2 == 1:
                    if dct["бинт"]:
                        universal.slow_text(chapter_1_text.heal())
                        dct["бинт"] = False
                        continue
                    else:
                        universal.slow_text(chapter_1_text.No_heal())
                        continue
                if var2 == 2:
                    universal.slow_text(chapter_1_text.punch_door())
                    break
                elif var2 == 3:
                    universal.slow_text(chapter_1_text.punch_door_2())
                    break
time.sleep(5)
print('\n'*20)