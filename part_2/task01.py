a = int(input('Введите первое число a >>> '))
b = int(input('Введите второе число b >>> '))
c = a * b
while a != b:

    if a > b:
        a -= b
    else:
        b -= a
else:
    nok = int(c / a)
    print(f"НОД = {a} \nНОК = {nok}")
