number = float(input("Введите число a-->"))
power = int(input("Введите числа n -->"))

result = 1
temp = number
n = power

while n > 0:
    if n & 1:
        result *= temp
    temp *= temp
    n >>= 1

print(f"Результат возведения равен: {result}")