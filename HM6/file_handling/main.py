from write_files import *
from read_files import *
from copy_delete_files import *

while True:
    print("Выберите что хотите сделать с файлом: ")
    print("1) Создать файл")
    print("2) Прочитать файл")
    print("3) Копирование и удаление")
    print("0) Выход")
    num = int(input("Напиши цифру: ").strip())
    
    if num == 1:
        while True:
            print("Выбери:")
            print("1) Создать файл")
            print("2) Добавить запись в файл(если существует)")
            print("0) Выход")
            num = int(input("Напиши цифру: ").strip())
            if num == 0:
                break
            if num == 1:
                create_new_f()
            if num == 2:
                write_smth()
    elif num == 2:
        while True:
            print("Выбери:")
            print("1) Прочитать все")
            print("2) Прочитать одну строку")
            print("3) Прочитать весь файл списком")
            print("0) Выход")
            num = int(input("Напиши цифру: ").strip())
            if num == 0:
                break
            if num == 1:
                read_one()
            if num == 2:
                read_two()
            if num == 3:
                read_three()
    elif num == 3:
        while True:
            print("Выбери:")
            print("1) Копировать")
            print("2) Удалить")
            print("0) Выход")
            num = int(input("Напиши цифру: ").strip())
            if num == 0:
                break
            if num == 1:
                copy()
            if num == 2:
                delet()
    elif num == 0:
        break
            
