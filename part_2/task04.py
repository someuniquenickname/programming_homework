import random

n = int(input('Введите количество элементов массива (N < 1000) >>> '))
array = []

for i in range(n):

    m = random.randint(0, 100)
    array.append(m)

print(f"Массив: {array} \nПеревернутый массив: {array[::-1]}")
