# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)
import random

lenght_lst = int(input("Введите длину списка: "))
my_lst = [random.randint(0, 50) for _ in range(lenght_lst)]
print(my_lst)
count = 0
new_lst = []
for index in range(lenght_lst):
    if my_lst[index-2] < my_lst[index - 1] > my_lst[index]:
        count += 1
        new_lst.append(my_lst[index-1])
print(new_lst)
print(count)

