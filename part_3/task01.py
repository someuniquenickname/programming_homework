import random
s = input("Количество чисел : ")
with open("./files/data.txt", "w") as file:
    for i in range(int(s)):
        file.write(str(random.randint(1,30)) + '\n')