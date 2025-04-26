try:
    from math import log, exp

    print('Попрошу ввести значение a в степени x.')
    a = float(input('Введите значение a = '))
    x = float(input('Введите значение x = '))

    if a > 0:
        b = exp(x * log(a))
        print('Результат', b)
    else:
        if not int(x) == x:
            print('Нельзя возвести отрицательное число в нецелую степень')
        else:
            b = 1
            i = 0
            while i < x:
                b = b * a
                i += 1
            if x > 0:
                b = b
            else:
                b = 1 / b
            print('Результат:', b)

except ValueError:
    print('Ошибка, пожалуйста, следуйте указанным программой.')
