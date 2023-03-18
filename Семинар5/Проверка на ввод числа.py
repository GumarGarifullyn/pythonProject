def input_int():
    while True:
        number = input("Введите число: ")
        try:
            if 0 < int(number) <= 100:
                return int(number)
            else:
                print("Число должно быть от 1 до 100")
        except:
            print("Это не число. Повторите ввод")


input_int()