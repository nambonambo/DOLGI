import os


os.mkdir("test_dir")

os.makedirs("first/sec/trird", exist_ok=True)

print(os.listdir("."))

print(os.getcwd())