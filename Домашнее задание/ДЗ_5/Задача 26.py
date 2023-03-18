# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree_num(num1, num2):

    if num2 == 0:
        return 1
    else:
        return num1 * degree_num(num1, num2 - 1)

num1 = int(input('Введите число: '))
num2 = int(input("Введите степень, в которую нужно возвести число: "))
print(f'{num1} в степени {num2} -> {degree_num(num1, num2)}')
print(num1**num2)
