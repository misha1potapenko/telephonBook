
def write_file():
    with open("test.txt", "a", encoding="UTF-8") as file:
        name = input("Привет, введите свое имя: ")
        file.write(f"{name}\n")
        number = input("Введите свой номер телефона: ")
        file.write(f"{number}\n")