# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
import random
import math


my_list = [random.randint(0, 99) for _ in range(20)]    # создан рандомный список
print(my_list)
num_user = int(input('Введите число: '))                     # пользователь вводит свое число
lst2 = []                                                                        # создаем второй список, чтобы записать
                                                                                    # в него значения разности между элементами
for elem in my_list:                                                       # первого списка и числа пользователя
    lst2.append(int(((elem - num_user)*(elem - num_user))**0.5))       # чем меньше  значение модуля второго списка
print(lst2)                                                                                           # тем ближе данное значение к числу пользователя
print(my_list[lst2.index(min(lst2))])



