import random

with open("part_3/files/fio2.txt", "r") as file:
    file2 = open("part_3/files/mark.csv", "w")
    for name in file.read().lower().strip().split("\n"):
        temp = [',']
        for i in range(random.randint(1,10)):
            temp.append(str(random.randint(2,5))+",")
        #print(temp)
        result = name + ''.join(temp)
        file2.write(result + "\n")
        
        
file.close()
file2.close()