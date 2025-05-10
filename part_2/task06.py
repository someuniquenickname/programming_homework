N = int(input('Введите N (N < 50) >>> '))

if N >= 50 or N <= 0:
    print('N должно быть меньше 50-ти')
else:

    F = [0, 1]

    for i in range(N):

        F.append(F[i-1]+F[i-2])

    print('Последовательность Фибоначчи: ')
    print(*F[:N])
