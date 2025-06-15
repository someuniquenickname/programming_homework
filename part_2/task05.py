import random

n = int(input('Введите количество элементов массива (N < 10) >>> '))
matrix = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]

print(f"Матрица:")
for row in matrix:
    print(*row)

diagonal_1 = sum(matrix[i][i] for i in range(n))
diagonal_2 = sum(matrix[i][n - i - 1] for i in range(n))

print(f'Сумма главной диагонали = {diagonal_1}')
print(f'Сумма побочной диагонали = {diagonal_2}')