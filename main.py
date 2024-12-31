from write import write_file
from read import read_file



def read_write():
    while True:
        try:
            choose = int(input("Привет, нажми цифру 1, если ты хочешь записать новые данные в телефонную книгу и "
                  "2 если хочешь прочитать книгу "
                               "3 если хочешь выйти  "))
            if choose == 1:
                write_file()
            elif choose == 2:
                read_file()
            elif choose == 3:
                break
            else:
                print("Я тебя не понимаю, выбери одну из цифр 1 2 3")
        except ValueError:
            print("Вы выбрали непонятные символы")
read_write()