line = str(input("-->"))
result = ''
left = 0
right = 2
for i in range(len(line)//3):
    result += line[left:right]
    left += 3
    right += 3

print(result)