# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

num = int(input('Введите число: '))
degree_2 = 0
print(f'{num} -> ', end=" ")
while num >= 2**degree_2:
    print(2**degree_2, end=' ')
    degree_2 +=1
print(f'\n {degree_2}')