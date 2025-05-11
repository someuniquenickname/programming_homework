N = int(input('Введите количество строк (N < 10) >>> '))

if N >= 10 or N <= 0:
    print('N должно быть положительном и меньше 10-ти')
else:
    matrix = []
    M = 1
    for i in range(N):
        row = []
        for j in range(N):
            row.append(M)
            M += 1
        matrix.append(row)

print("Матрица:")

for row in matrix:
    print(*row)
