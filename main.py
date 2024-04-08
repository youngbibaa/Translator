from stmt import stmt_main, stmt_storage
from database import (
    log_in,
    create_table,
    add,
    select,
    translate,
    LANGUAGES,
    table_exists,
)
import time

lang_base = {"default_lan": "en", "lang_to_trans": "ru"}

if not table_exists("base"):
    create_table(stmt_main["create"])
if not table_exists("storage"):
    create_table(stmt_storage["create"])

while True:
    print("Меню:")
    print("1. Регистрация")
    print("2. Вход в аккаунт")
    print("3. Выйти")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        nickname = input("Введите никнейм: ")
        password = input("Введите пароль: ")
        add(stmt_main["add"], (nickname, log_in(password)))
        print("Вы зарегистрировались!")
    elif choice == 2:
        nickname = input("Введите никнейм: ")
        password = input("Введите пароль: ")
        base = select(stmt_main["select"], (nickname,))
        if len(base) == 0:
            print("Аккаунт не зарегистрирован!")
            continue
        elif log_in(password) == base[0][1]:
            print("Вы успешно вошли в аккаунт!")
            base.clear()
            while True:
                print("Выберите действие: ")
                print("1. Выбор языков для перевода")
                print("2. Перевести текст")
                print("3. Текущие языки")
                print("4. Смена языков")
                print("5. Вывод истории поиска пользователя")
                print("6. Выйти")
                action = int(input("Выберите действие: "))
                if action == 1:
                    for key, value in LANGUAGES.items():
                        print(f"{value} - {key}")
                    default_language = input("Выберите язык текста: ")
                    language_to_translate = input("Выберите язык перевода:")
                    if (default_language not in LANGUAGES.keys()) or (
                        language_to_translate not in LANGUAGES.keys()
                    ):
                        print("Неправильный ввод, повторите еще раз!")
                        continue
                    lang_base["default_lan"] = default_language
                    lang_base["lang_to_trans"] = language_to_translate
                    time.sleep(1)
                elif action == 2:
                    if len(lang_base) == 0:
                        print("Вы не выбрали языки!")
                        continue
                    text = input("Введите текст для перевода: ")
                    add(stmt_storage["add"], (nickname, text))
                    translate(
                        text,
                        lang_base.get("default_lan"),
                        lang_base.get("lang_to_trans"),
                    )
                    time.sleep(3)
                elif action == 3:
                    print(
                        f"{LANGUAGES.get(lang_base.get('default_lan'))} -> {LANGUAGES.get(lang_base.get('lang_to_trans'))}"
                    )
                    time.sleep(1)
                elif action == 4:
                    first = lang_base.get("default_lan")
                    second = lang_base.get("lang_to_trans")
                    lang_base["default_lan"] = second
                    lang_base["lang_to_trans"] = first
                    print(
                        f"{LANGUAGES.get(lang_base.get('default_lan'))} -> {LANGUAGES.get(lang_base.get('lang_to_trans'))}"
                    )
                    time.sleep(1)
                elif action == 5:
                    print("История поиска пользователя")
                    story = select(stmt_storage["select"], (nickname,))
                    for i in story:
                        print(i[1])
                    time.sleep(2)
                elif action == 6:
                    break
                else:
                    print("Неверный выбор. Пожалуйста, выберите снова.")
        else:
            print("Введен неправильный пароль!")
    elif choice == 3:
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
