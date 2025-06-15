N = int(input('Введите N (N < 50) >>> '))

if N >= 50 or N <= 0:
    print('N должно быть меньше 50-ти')
else:
    a, b = 0, 1
    F = [a, b]
    for i in range(2, N):
        a, b = b, a + b
        F.append(b)
    
    print('Последовательность Фибоначчи: ')
    print(*F[:N])