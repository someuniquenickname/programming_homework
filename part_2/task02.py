import math

n = int(input('Введите количество чисел (N < 1000) >>> '))
numbers = []

for i in range(n):
    n_i = float(input(f"Введите число №{i+1}: "))
    numbers.append(n_i)

x_m = sum(numbers)/n

dispersion = sum((x - x_m) ** 2 for x in numbers) / n

std = math.sqrt(dispersion)

print(f"\nСреднее значение: {x_m} \nДисперсия: {dispersion} \nСреднее квадратическое отклонение: {std}")
