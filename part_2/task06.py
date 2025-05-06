run = 1
while run:
    try:
        n = int(input("N --> "))
        if n >= 0 and n < 50:
            run = 0
        else:
            print("Введите корректное число N (большее или равное нулю, но меньшее, чем 50)")
    except:
        print("Введите корректное число N (большее или равное нулю)")

if n == 0:
    print("Nothing")
if n == 1:
    print("0")
if n == 2:
    print("0; 1")
fiba_numbers = [0, 1]

for i in range(n-2):
    fiba_numbers.append(fiba_numbers[-1] + fiba_numbers[-2])

print("; ".join(map(str,fiba_numbers)))
