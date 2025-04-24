n = int(input('Введите n >>> '))


if n <= 0:
   print('n должно быть положительном числом')
else:
   k = 0
   for i in range(0, n + 1):
       k += i
   print(f"Сумма данного n: {k}")
