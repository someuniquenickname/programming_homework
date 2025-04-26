number = float(input("Введите число a-->"))
power = int(input("Введите числа n -->"))

binpower = str(bin(n))[::-1][:-2]
result = 1

for i in binpower:
    if i == '0':
        pass
    elif i == '1':
        result *= number
    number *= number

print(f"Задача выполнена не более чем за {len(binpower)} итераци(и/й), и результат возведения равен: {result}")
