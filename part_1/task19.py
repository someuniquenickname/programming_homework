n = int(input('Введите n >>> '))

if n <= 0:
   print('n должно быть положительном числом')
else:
   result = n * (n + 1) // 2
   print(result)