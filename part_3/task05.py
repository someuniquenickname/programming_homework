with open('./files/mark.csv', 'r') as file:
    file2 = open("./files/result.csv", "w")
    for line in file:
        parts = line.strip().split(',')
        name = parts[0]
        marks = [int(x) for x in parts[1:]]
        avg = sum(marks) / len(marks)
        file2.write(f"{name}: {avg:.2f}\n")