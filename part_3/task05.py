with open("part_3/files/mark.csv", "r") as file:
    file2 = open("part_3/files/result.csv", 'w')
    temp_name = ''
    temp = 0
    count = 0
    for name in file.read().lower().strip().split("\n"):
        for digit in name.split(','):
            if digit.isdigit() == False and digit != '':
                temp_name = digit
            elif digit.isdigit() == True:
                temp = temp + int(digit)
                count += 1
        temp = float(temp / count)
        file2.write(temp_name + ',' + str(temp) + '\n')
        temp = 0
        count = 0
        temp_name = ''
file.close()
file2.close()