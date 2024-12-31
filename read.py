
def read_file():
    with open(r"test.txt", "r", encoding="UTF-8") as file:
        for line in file:
            print(line)
