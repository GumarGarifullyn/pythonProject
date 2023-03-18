# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
#
# def prostoe_chislo (num: int):
#     if not num % 2 and num != 2:
#         for i in range(3, 2):
#             if not num % 2:
#                 return print(f"{chislo} не является простым числом")
#     return print(f'{chislo} является простым числом')
#
# chislo = int(input('Введите число: '))
# print(prostoe_chislo(chislo))

a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")