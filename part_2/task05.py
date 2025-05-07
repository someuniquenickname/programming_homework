import random

n = int(input('Введите количество элементов массива (N < 10) >>> '))

matrix = [[random.randint(0, 9) for i in range(n)] for j in range (n)]

print(f"Матрица:")
for row in matrix:
    print(*row)

diagonal_1 = 0
diagonal_2 = 0

for i in range(n):
    diagonal_1 += matrix[i][i]
    diagonal_2 += matrix[i][n - i - 1]

print(f'Сумма главной диагонали = {diagonal_1}')
print(f'Сумма побочной диагонали = {diagonal_2}')
