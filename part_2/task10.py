line = str(input("-->"))

for i in range(len(line)):
    symbol = line[i:i+1]
    if symbol in ",.:;-!?":
        line = line[:i] + " " + line[i+1:]

print(len(line.split()))