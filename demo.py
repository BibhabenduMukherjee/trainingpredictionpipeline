from pathlib import Path

path_tobe_read = Path("demo1.txt")

if path_tobe_read.exists():
    with open(path_tobe_read, "r") as file:
        content = file.read()
        print(content)
else:
    print("file path is not exist")