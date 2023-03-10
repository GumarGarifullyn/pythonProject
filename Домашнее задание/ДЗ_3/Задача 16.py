# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
import random

num = int(input("Введите число от 0 до 5, повторяющееся в списке: "))
lenght_list = int(input('Введите длину листа: '))
my_list = [random.randint(0, 5) for _ in range(lenght_list)]
print(my_list)
count = 0
for elem in my_list:
    if elem == num:
        count += 1
print(count)
