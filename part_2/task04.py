import random

n = int(input('Введите количество элементов массива (N < 1000) >>> '))
array = [random.randint(0, 100) for _ in range(n)]

print(f"Массив: {array} \nПеревернутый массив: {array[::-1]}")