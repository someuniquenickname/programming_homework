import random
s = input("Количество чисел : ")
file = open("part_3/files/data.txt", "w")
for i in range(int(s)):
    file.write(str(random.randint(1,30)) + ' ')
file.close()