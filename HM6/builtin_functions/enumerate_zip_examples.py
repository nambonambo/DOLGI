names = ["Ali", "Dana", "Max"]
ages = [18, 20, 22]

for i, name in enumerate(names):
    print(i, name)

for name, age in zip(names, ages):
    print(name, age)