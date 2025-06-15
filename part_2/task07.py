N = int(input('Введите количество строк (N < 10) >>> '))

if N >= 10 or N <= 0:
    print('N должно быть положительном и меньше 10-ти')
else:
    matrix = [[i * N + j + 1 for j in range(N)] for i in range(N)]
    
    print("Матрица:")
    for row in matrix:
        print(*row)