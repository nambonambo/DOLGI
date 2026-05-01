import os
import shutil

# создаём файл
with open("file.txt", "w") as f:
    f.write("test")

# создаём папку
os.makedirs("target", exist_ok=True)

# перемещение
shutil.move("file.txt", "target/file.txt")
print("File moved")

# копирование
shutil.copy("target/file.txt", "file_copy.txt")
print("File copied")