# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

import random
# lst1 = []
# num_len = int(input('Введите число элементов списка: '))
# num2 = int(input("Введите число на которое следует сместить элементы в списке: "))
# for i in range(num_len):
#     lst1.append(random.randint(0, 100))
#     i += 1
# print(lst1)
# lst2 = lst1[num2::] + lst1[:num2]
# print(lst2)

my_list = [random.randint(0, 100) for i in range(random.randint(0, 20))]
print((my_list))
for elements in my_list:
     print(elements, end="   ")
print()
for indexes in range(len(my_list)):
     print(indexes, end=", ")
print()
shift = int(input("Введите величину сдвига: "))
for i in range(shift):
     my_list.insert(0, my_list.pop(-1))

print(my_list)