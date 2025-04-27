import random

n = int(input('Введите количество элементов массива (N < 100) >>> '))
array = []

for i in range(n):

    m = random.randint(0, 100)
    array.append(m)

max = max(array)
min = min(array)

print('Массив:', array)
print(f"Максимальное значение: {max} \nМинимальное значение: {min}")
