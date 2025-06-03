n = int(input('Введите n >>> '))
result = 0

if n <= 0:
   print('n должно быть положительном числом')
else:
   if n % 2 == 0:
      result = int((n+1)*n/2)
   if n % 2 == 1:
      result = int(n//2+1)*n


print(result)