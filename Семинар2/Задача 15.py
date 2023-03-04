# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9



import random
import math
n = int(input('Введите количество арбузов: '))
weight_watermelon = []
i = 0
while i < n:
    weight_watermelon.append(random.randint(1000,30000))
    i += 1
print(f'{n} -> {weight_watermelon}')
print(f'Вес самого легкого арбуза = {min(weight_watermelon)}, а самого тяжелого = {max(weight_watermelon)}')


# import random
# numbers_watermelon = int(input("Введите количество арбузов для сравнения"))
# weight_1 = random.randint(1,100)
# print(f'Вес первого арбуза {weight_1}')
# max_weight = weight_1
# min_weight = weight_1
# for i in range(numbers_watermelon-1):
#     weight = random.randint(1,100)
#     if weight > max_weight:
#         max_weight = weight
#     elif weight < min_weight:
#         min_weight = weight
# print(min_weight,max_weight)
















