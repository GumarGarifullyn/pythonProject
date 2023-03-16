# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

my_str = input('Введите буквы через пробел: ')
my_list = my_str.split()
print(my_list)
for elem in my_list:
    count = 0
    for index in range(len(my_list)):
        if my_list[index] == elem:
            if count == 0:
                my_list[index] == my_list[index]
            else:
                my_list[index] = str(my_list[index] + '_' + str(count))
            count += 1
print(my_list)

my_dict = {}
# for el in my_str:
#     my_dict[el] = my_dict.get(el, 0) + 1
#     if my_dict[el] == 1:
#         print(el, end=', ')
#     else:
#         print(f'{el}_{my_dict[el] - 1}', end=', ')

for i in my_list:
    my_dict[i] = my_dict.get(i, 0) + 1
    print(i if my_dict.get(i) == 1 else f'{i}_{my_dict.get(i) - 1}', end=' ')
print('\n' + f'{my_dict}')