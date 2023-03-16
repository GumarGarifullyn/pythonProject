# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
import random
num = int(input('Введите кол-во оценок у Василия: '))
evaluation = [random.randint(1, 5) for _ in range(num)]
print(evaluation)
# index = 0
# while index  < len(evaluation):
#     if evaluation[index] >= 4:
#         evaluation[index] = min(evaluation)
#     index += 1
# print(evaluation)

for i in range(len(evaluation)):
    if evaluation[i] > 3:
        evaluation[i] = min(evaluation)
print(evaluation)
