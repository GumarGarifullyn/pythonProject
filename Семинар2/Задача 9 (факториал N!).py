# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

n = int(input("Введите число, чтобы узнать значение его факториала: "))
multiplication = 1
while n >= 0:
    if n > 0:
        multiplication = n*multiplication
    else:
        multiplication = multiplication*1
    n -= 1
print(multiplication)
