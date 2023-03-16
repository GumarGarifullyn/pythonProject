# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

lenght_list1 = int(input("Введите длину первого списка: "))
lenght_list2 = int(input("Введите длину второго списка: "))
list1 = [random.randint(0, 5) for _ in range(lenght_list1)]
print(list1)
list2 = [random.randint(0, 5) for _ in range(lenght_list2)]
print(list2)
set1 = set(list1).intersection(list2)
print(set1)
print(sorted(set1))


a = {11, 8, 90, 54, 7, 0, 67}
b = {0, 90, 7, 67}
print(a & b)
print(sorted(a & b))