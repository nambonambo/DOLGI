
def read_one():
    with open("data.txt", "r") as f:
        print("READ:")
        print(f.read())
        
def read_two():
    with open("data.txt", "r") as f:
        print("READLINE:")
        print(f.readline())
def read_three():
    with open("data.txt", "r") as f:
        print("READLINES:")
        print(f.readlines())