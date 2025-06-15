line = input("-->")
print(''.join(line[i:i+2] for i in range(0, len(line), 3)))