line = str(input("-->"))

upper_case = 0
lower_case = 0

for i in range(len(line)):
    symbol = line[i:i+1]
    if symbol == symbol.upper():
        upper_case += 1
    elif symbol == symbol.lower():
        lower_case += 1
    else:
        print("ERROR")

print(f"{lower_case=},{upper_case=}")
