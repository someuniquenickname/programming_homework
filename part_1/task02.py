import math

a = float(input("Введите a >>> "))
b = float(input("Введите b >>> "))
c = float(input("Введите c >>> "))

if a == 0:
   print("Это не квадратное уравнение.")
else:
   d = b*b - 4*a*c
   
   if d > 0:
       sqrt_d = math.sqrt(d)
       inv_2a = 1/(2*a)
       x1 = (-b + sqrt_d) * inv_2a
       x2 = (-b - sqrt_d) * inv_2a
       print(f" x1 = {x1}, x2 = {x2}")
   elif d == 0:
       x = -b / (2*a)
       print(f"x = {x}")
   else:
       print("Нет действительных корней.")