import math

a = float(input("Введите первую сторону >>> "))
b = float(input("Введите вторую сторону >>> "))
c = float(input("Введите третью сторону >>> "))

if a + b <= c or a + c <= b or b + c <= a:
   print("Такого треугольника нет")
else:
   p = (a+b+c)*0.5
   print(f"Площадь треугольника: {math.sqrt(p * (p - a) * (p - b) * (p - c))}")