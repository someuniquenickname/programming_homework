run = 1
while run:
    try:
        n = int(input("N --> "))
        if n > 0:
            run = 0
    except:
        print("Введите корректное число N")


matrix = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        run = 1
        while run:
            try:
                matrix[i][j] = int(input(f"Строка {i} стоолбец {j} -->"))
                run = 0
            except:
                print("Неверный ввод")
sum_main = 0
sum_side = 0

print("\n")

for i in range(n):
    sum_main += matrix[i][i]
    sum_side += matrix[i][n-i-1]
    for j in range(n):
        print(matrix[i][j], "\t", end='')
    print("\n")
print(f"Сумма главной диагонали равна {sum_main}, а побочной {sum_side}\n")
