import shutil
import os

def copy():
    try:
        shutil.copy("data.txt", "copy.txt")
        print("Скопировано")
    except:
        print("файла нет")

def delet():
    if os.path.exists("copy.txt"):
        os.remove("copy.txt")
        print("Файл удален")
    else:
        print("Файл не существует")