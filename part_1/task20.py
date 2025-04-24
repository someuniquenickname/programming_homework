n = int(input('Введите n >>> '))


if n <= 0:
   print('n должно быть положительном числом')
else:
   k = 1
   for i in range(1, n + 1):
       k *= i
   geom_prog = k ** (1 / n)
   print(f"Среднее геометрическое произведение от 1 до {n}: {geom_prog}")
