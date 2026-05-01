import csv
from connect import get_connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created")


def insert_from_csv(filename="contacts.csv"):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV data inserted")


def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added")


def update_contact():
    old_name = input("Old name: ")
    new_name = input("New name (or enter to skip): ")
    new_phone = input("New phone (or enter to skip): ")

    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_name, old_name))

    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, old_name))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated")


def search_contacts():
    print("1) By name")
    print("2) By phone prefix")
    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Name: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (name,))

    elif choice == "2":
        prefix = input("Phone prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_contact():
    value = input("Delete by name or phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name=%s OR phone=%s",
        (value, value)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact deleted")


def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1) Create table")
        print("2) Insert from CSV")
        print("3) Add contact")
        print("4) Update contact")
        print("5) Search contacts")
        print("6) Delete contact")
        print("0) Exit")

        choice = input("Select: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            search_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()