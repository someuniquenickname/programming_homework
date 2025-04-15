num = str(input(">>>"))
localmin = 0
localmax = 10
for i in num:
    if int(i) > localmax:
        localmax = int(i)
    if int(i) < localmin:
        localmin = int(i)
print(f"Минимальная цифра в числе - {localmin}, максимальная - {localmax} ")

