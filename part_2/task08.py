N = int(input('Введите количество строк (N < 10) >>> '))

if N >= 10 or N <= 0:
    print('N должно быть положительном и меньше 10-ти')

else:
    matrix = [[0] * N for _ in range(N)]

    num = 1
    left, right = 0, N - 1
    top, bottom = 0, N - 1

    while left <= right and top <= bottom:

        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1


        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1


        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    width = len(str(N * N))
    for row in matrix:
        print(" ".join(f"{x:>{width}}" for x in row))
