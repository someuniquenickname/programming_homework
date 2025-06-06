string  = str(input("-->")).strip()
length = len(string)
run = True
for i in range(len//2):
    if string[len - i] != string[i]:
        run = False


print(run)


#Второй вариант
# l = input()
# print(l == l[::-1]) 