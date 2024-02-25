import time
import sys
from funks import universal, ends
from texts import chapter_3_text
import random
# Список слов для шифрования
words = ['подавление', 'кровь', 'оружие', 'хаос', 'паника', 'выживание', 'разрушение', 'жертвы', 'инфекция', 'отчаяние']

# Расшифровка азбуки Морзе (русские буквы)
morse_code_dict_rus = {
    'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..',
    'е': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---',
    'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---',
    'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-',
    'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
    'щ': '--.-', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-',
}


print(chapter_3_text.logo())
print(31*' ',end='')
universal.slow_text("Глава третья Финал: Последний шанс \n\n", _time=0.09)
time.sleep(1)
universal.slow_text(chapter_3_text.description_situation())

basement = 0

universal.slow_text("ДЕЛАЙ ВЫБОР (ДУМАЙ! ЭТО ВАЖНО): \n")
print("[1] Спуститься в подвал! \n"
      "[2] Остаться наверху! \n")
while True:
    try:
        where = int(input("Выбери действие: "))
        if where < 1 or where > 2:
            print("введите число от 1 до 2")
        else:
            break
    except ValueError:
        print("введите ЧИСЛО от 1 до 2")
if where == 1:
    basement = True
    universal.slow_text(chapter_3_text.basement())
    input("Нажми Enter чтобы осмотреть план помещения.\n")
    universal.slow_text(chapter_3_text.basement_1())
else:
    basement = False


if basement:
    input("Нажми Enter чтобы начать\n\n")
    current_room = "Главный зал"
    lever_1 = False
    lever_2 = False
    lever_3 = False
    lever_4 = False
    medicament = False
    start_time = time.time()
    while not medicament and time.time() - start_time <10:
        if current_room == "Главный зал":
            if lever_1 and lever_2 and lever_3 and lever_4:
                universal.slow_text("Я Нахожусь в главном зале горит 1,2,3 и 4 лампочка, похоже все готово.:\n")
            elif lever_1 and lever_2 and lever_3:
                universal.slow_text("Я Нахожусь в главном зале горит 1,2 и 3 лампочка:\n")
            elif lever_1 and lever_2:
                universal.slow_text("Я Нахожусь в главном зале горит 1 и 2 лампочка:\n")
            elif lever_1:
                universal.slow_text("Я Нахожусь в главном зале горит 1 лампочка:\n")
            else:
                universal.slow_text("я в главном зале\n")
            print("[1] В коридор А.\n"
                  "[2] В коридор Б.\n"
                  "[3] К центральной двери\n", )
            while True:
                try:
                    where = int(input("Выбери действие: \n"))
                    if where < 1 or where > 3:
                        print("введите число от 1 до 3")
                    else:
                        break
                except ValueError:
                    print("введите ЧИСЛО от 1 до 3")
            if where == 1:
                universal.slow_text("Вы идете в коридор А\n")
                current_room = "А"
            elif where == 2:
                universal.slow_text("Вы идете в коридор Б\n")
                current_room = "Б"
            else:
                universal.slow_text("Вы идете к центральной комнате\n")
                current_room = "Дверь к лекартсву"

        elif current_room =="Дверь к лекартсву":
            if lever_1 and lever_2 and lever_3 and lever_4:
                universal.slow_text("Получилось дверь открылась и вы прошли внутрь.\n")
                current_room = "лекарство"
            else:
                universal.slow_text("Нужно как-то активировать все 4 лампочки.\n")
                current_room = "Главный зал"

        elif current_room == "А":
            universal.slow_text("Вы в коридоре А:\n")
            print("[1] В комнату 1\n"
                  "[2] В комнату 3\n"
                  "[3] В Главный зал\n", )
            while True:
                try:
                    where = int(input("Выбери действие: \n"))
                    if where < 1 or where > 3:
                        print("введите число от 1 до 3")
                    else:
                        break
                except ValueError:
                    print("введите ЧИСЛО от 1 до 3")
            if where == 1:
                universal.slow_text("Вы заходите в 1 комнтау, здесь панель с зашифрованым паролем от 2 двери\n")
                current_room = "1"
            elif where == 2:
                if lever_2:
                    universal.slow_text("Вы заходите в 3 комнтау, здесь панель с зашифрованым паролем от 4 двери\n")
                    current_room = "3"
                else:
                    universal.slow_text("нужно активировать предыдущую панель.\n")
            else:
                universal.slow_text("Вы возвращаетесь\n")
                current_room = "Главный зал"

        elif current_room == "Б":
            universal.slow_text("Вы в коридоре Б:\n")
            print("[1] В комнату 2\n"
                  "[2] В комнату 4\n"
                  "[3] В Главный зал\n", )
            while True:
                try:
                    where = int(input("Выбери действие: \n"))
                    if where < 1 or where > 3:
                        print("введите число от 1 до 3")
                    else:
                        break
                except ValueError:
                    print("введите ЧИСЛО от 1 до 3")
            if where == 1:
                if lever_1:
                    universal.slow_text("Вы заходите в 2 комнтау, здесь панель с зашифрованым паролем от 3 двери\n"
                                        "(шифр цезаря c шагом в 2)\n")
                    current_room = "2"
                else:
                    universal.slow_text("нужно активировать предыдущую панель.\n")
            elif where == 2:
                if lever_3:
                    universal.slow_text("Вы заходите в 4 комнтау, здесь панель с зашифрованым паролем финальная\n"
                                        "(шифр цезаря c шагом в 2)\n")
                    current_room = "4"
                else:
                    universal.slow_text("нужно активировать предыдущую панель.\n")
            else:
                universal.slow_text("Вы возвращаетесь\n")
                current_room = "Главный зал"

        elif current_room == "1":
            if lever_1:
                universal.slow_text("Я уже здесь все сделал и выходишь в коридор")
                current_room = "А"
            else:
                # Выбор случайного слова для шифрования
                word = random.choice(words)

                # Шифрование слова в азбуке Морзе
                encrypted_word = ' '.join([morse_code_dict_rus.get(letter, ' ') for letter in word])

                # Запрос у пользователя расшифрованной версии слова
                user_input = input(f"Зашифрованное слово: {encrypted_word}\nРасшифруйте слово: ")

                # Проверка правильности расшифровки
                if user_input.lower() == word:
                    print("Пароль правильный.")
                    lever_1 = True
                else:
                    print("Пароль неправильный.")
                    current_room = "1"

        elif current_room == "2":
            if lever_2:
                universal.slow_text("Я уже здесь все сделал и выходишь в коридор")
                current_room = "Б"
            else:
                def encrypt(word):
                    encrypted_word = ""
                    for letter in word:
                        if 'а' <= letter <= 'я':
                            shifted_ascii_code = (ord(letter) - ord('а') - 2) % 32 + ord('а')
                            encrypted_word += chr(shifted_ascii_code)
                        else:
                            encrypted_word += letter
                    return encrypted_word

                # Выбираем случайное слово из списка
                random_word = random.choice(words)

                # Шифруем это слово
                encrypted_random_word = encrypt(random_word)

                print(f"Зашифрованное слово: {encrypted_random_word}")

                # Пользователь вводит расшифрованное слово
                user_input = input("Введите расшифрованное слово: ")

                # Проверка правильности расшифровки
                if user_input == random_word:
                    print("Пароль правильный.")
                    lever_2 = True
                else:
                    print("Пароль неправильный.")
                    current_room = "2"

        elif current_room == "3":
            if lever_3:
                universal.slow_text("Я уже Здесь все сделал и выходишь в коридор")
                current_room = "А"
            else:

                # Выбор случайного слова для шифрования
                word = random.choice(words)

                # Шифрование слова в азбуке Морзе
                encrypted_word = ' '.join([morse_code_dict_rus.get(letter, ' ') for letter in word])

                # Запрос у пользователя расшифрованной версии слова
                user_input = input(f"Зашифрованное слово: {encrypted_word}\nРасшифруйте слово: ")

                # Проверка правильности расшифровки
                if user_input.lower() == word:
                    print("Пароль правильный.")
                    lever_3 = True
                else:
                    print("Пароль неправильный.")
                    current_room = "3"

        elif current_room == "4":
            if lever_4:
                universal.slow_text("Я уже здесь все сделал и выходишь в коридор")
                current_room = "Б"
            else:
                def encrypt(word):
                    encrypted_word = ""
                    for letter in word:
                        if 'а' <= letter <= 'я':
                            shifted_ascii_code = (ord(letter) - ord('а') - 2) % 32 + ord('а')
                            encrypted_word += chr(shifted_ascii_code)
                        else:
                            encrypted_word += letter
                    return encrypted_word


                # Выбираем случайное слово из списка
                random_word = random.choice(words)

                # Шифруем это слово
                encrypted_random_word = encrypt(random_word)

                print(f"Зашифрованное слово: {encrypted_random_word}")

                # Пользователь вводит расшифрованное слово
                user_input = input("Введите расшифрованное слово: ")

                # Проверка правильности расшифровки
                if user_input == random_word:
                    print("Пароль правильный.")
                    lever_4 = True
                else:
                    print("Пароль неправильный.")
                    current_room = "4"

        elif current_room == "лекарство":
            universal.slow_text(chapter_3_text.medicament())
            medicament = True


    if medicament:
        input("Нажми Enter чтобы продолжить\n")
        universal.slow_text(chapter_3_text.posle())
        input("Нажми Enter чтобы продолжить\n")
        universal.slow_text(ends.second_end())
        time.sleep(2)
        universal.slow_text("Вы медленно открывает глаза и осознаете, что ваше сознание погружено в туман....")
        sys.exit(1)
    else:
        universal.slow_text(chapter_3_text.no_time())
        time.sleep(3)
        universal.slow_text(ends.third_ens())
        time.sleep(2)
        universal.slow_text("Вы медленно открывает глаза и осознаете, что ваше сознание погружено в туман....")
        sys.exit(1)



else:
    universal.slow_text(chapter_3_text.ground())
    print("[1] Бежать через главную дверь.\n"
          "[2] Оборонять здание.\n"
          "[3] бежать через запасной выход.\n")
    while True:
        try:
            where = int(input("Выбери действие: \n"))
            if where < 1 or where > 3:
                print("введите число из перечисленных:")
            else:
                break
        except ValueError:
            print("введите ЧИСЛО из перечисленных:")
    if where == 1:
        universal.slow_text(chapter_3_text.run_door())
    elif where == 2:
        universal.slow_text(chapter_3_text.defender())
    elif where == 3:
        universal.slow_text(chapter_3_text.back_door())
time.sleep(3)
universal.slow_text(ends.first_end_4())
sys.exit(1)