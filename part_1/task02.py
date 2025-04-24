import math


a = float(input("Введите a >>> "))
b = float(input("Введите b >>> "))
c = float(input("Введите c >>> "))


if a == 0:
   print("Это не квадратное уравнение.")
else:
   d = b**2 - 4 * a * c


   if d > 0:
       x1 = ((-b) + math.sqrt(d))/(2 * a)
       x2 = ((-b) - math.sqrt(d))/(2 * a)
       print(f" x1 = {x1}, x2 = {x2}")
   elif d == 0:
       x = (- b / (2 * a))
       print(f"x = {x}")
   else:
       print("Нет действительных корней.")
