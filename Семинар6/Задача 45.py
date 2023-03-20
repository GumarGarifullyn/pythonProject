# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284
def summa_deliteley(num):
    i = 1
    my_lst = []
    while i < num:
        if num % i == 0:
            my_lst.append(i)
        i += 1
    return sum(my_lst)


numb = int(input('Введите число: '))
# num_dict = {}
# for el in range(1, numb):
#     num_dict[el] = summa_deliteley(el)
#
# for key1, value1 in num_dict.items():
#     for key2, value2 in num_dict.items():
#         if key2 > key1:
#             if value1 == key2 and value2 == key1:
#                 print(f'{key1} {key2}')

for i in range(1, numb):
    if summa_deliteley(summa_deliteley(i)) == i and i < summa_deliteley(i):
        print(f'{i}, {summa_deliteley(i)}')