# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
import random

leght_lst1 = int(input("Введите длину списка: "))
lst1 = []
for i in range(leght_lst1):
    lst1.append(random.randint(0, 99))
print(lst1)
count = 0
for index in range(len(lst1)):
    if lst1[index] > lst1[index-1]:
        count += 1
print(count)
