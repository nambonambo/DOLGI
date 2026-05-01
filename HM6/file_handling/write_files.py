
    
def create_new_f():
    with open("data.txt", "w") as file:
        file.write("Напишите что-то...")
        
def write_smth():
    with open("data.txt", "a") as file:
        text = input("Напишите что-то: ")
        file.write("\n" + text)