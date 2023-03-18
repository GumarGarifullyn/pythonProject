# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3
import random

my_lst = [random.randint(0, 3) for _ in range(int(input('Введите длину списка: ')))]
print(my_lst)
count = 0
for elem in my_lst:
    if my_lst.count(elem) > 1:
        count += 1
print(count//2)

check_list = {}
ch_l = {}
for el in my_lst:
    if my_lst.count(el) > 1:
        check_list[el] = my_lst.count(el)
        ch_l[el] = my_lst.count(el) // 2
print(check_list)
print(ch_l)
print(sum((check_list.values())))
print(sum((ch_l.values())))