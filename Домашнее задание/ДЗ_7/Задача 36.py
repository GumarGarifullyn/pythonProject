# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# list_2 = [1,2,3,4,5,6,7,8,9,10]
# new_list = []
# new_str = ''
# for el in list_1:
#     print()
#     for elem in list_2:
#         a = el*elem
#         print(f"{a:=<5}", end=" ")
#
# print()
# print(new_list)
# print(new_str)
#
def print_operation_table(operation, num_rows=6, num_columns=6):
        for el in range(1, num_rows +1):
            print()
            for elem in range(1, num_columns+1):
                operation(el, elem)
                print(operation(el, elem), end=" ")

print_operation_table(lambda x, y: x*y,6,6)
