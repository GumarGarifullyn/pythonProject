# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

A = int(input("Введите число A>1: "))
fib_1 = 0
fib_2 = 1
fib_cur = 0
count = 1
while fib_cur < A:
    fib_cur = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = fib_cur
    count += 1
print(count if A == fib_cur else '-1')








