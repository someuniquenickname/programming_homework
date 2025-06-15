import random

with open('./files/fio2.txt', 'r') as f:
    names = [line.strip() for line in f if line.strip()]

with open('./files/mark.csv', 'w') as f:
    for name in names:
        marks = [str(random.randint(1, 10)) for _ in range(5)]
        f.write(name + ', ' + ', '.join(marks) + '\n')