# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import random
import math
my_list = [random.randint(1000, 9999) for _ in range(5)]
print(my_list)
new_list = []
num = (input("Введите цифру, которую нужно удалить из элементов списка: "))
for value in my_list:
    el = str(value).replace(num, '')
    new_list.append(el)
print(new_list)
summa = 0
for value in new_list:
    for elem in value:
        summa += int(elem)
    while summa > 9:
        for el in str(summa):
            summa += int(el)

    print(summa)

# for elem in new_list:
#     sum_num = sum([(int(el)) for el in elem])
#     if sum_num
#     print(sum_num)





