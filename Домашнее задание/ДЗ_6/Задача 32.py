# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
conditions_list = [int(input('Введите нижнюю границу заданного Вами диапазона: ')), int(input('Введите верхнюю границу заданного Вами диапазона: '))]
my_list = [random.randint(-10, 10) for _ in range(10)]
print(my_list)
index_list = []
for i in range(len(my_list)):
    if conditions_list[0] <= my_list[i] <= conditions_list[1]:
        index_list.append(i)
print(index_list)