from connect import get_connection

conn = get_connection()
cur = conn.cursor()


def show_all():
    cur.execute("SELECT * FROM contacts ORDER BY name")
    rows = cur.fetchall()
    for r in rows:
        print(r)


def upsert_user():
    name = input("Имя: ")
    phone = input("Телефон: ")
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Добавлено / обновлено")


def add_from_file():
    filename = "contacts.csv"

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            name, phone = line.strip().split(",")

            cur.execute(
                "CALL upsert_contact(%s, %s)",
                (name, phone)
            )

    conn.commit()
    print("Файл загружен в базу")


def pagination():
    limit = int(input("Сколько записей показывать: "))
    offset = int(input("С какого места начать: "))

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for r in rows:
        print(r)


def delete_user():
    value = input("Введите имя или телефон для удаления: ")
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    print("Удалено (если существовало)")


def menu():
    run = True

    while run:
        print("Телефонная книга")
        print("1) Вывести все записи")
        print("2) Добавить / обновить пользователя")
        print("3) Добавить пользователей из файла")
        print("4) Постраничный просмотр")
        print("5) Удаление пользователя")
        print("0) Выход")

        try:
            choice = int(input("Выберите действие: "))
        except ValueError:
            print("Введите число!")
            continue

        if choice == 1:
            show_all()

        elif choice == 2:
            upsert_user()

        elif choice == 3:
            add_from_file()

        elif choice == 4:
            pagination()

        elif choice == 5:
            delete_user()

        elif choice == 0:
            print("Выход из программы")
            run = False

        else:
            print("Неверный выбор")


if __name__ == "__main__":
    menu()