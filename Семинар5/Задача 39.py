# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random

length_list1 = int(input('Введите длину списка 1: '))
length_list2 = int(input('Введите длину списка 2: '))
list1 = [random.randint(0,10) for _ in range(length_list1)]
list2 = [random.randint(0,10) for _ in range(length_list2)]
temp_list = []
print(list1)
print(list2)
for elem in list1:
    if elem not in list2:
        temp_list.append(elem)
print(temp_list)