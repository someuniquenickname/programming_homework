line = str(input("-->"))
result = []
current = ""

for char in line:
    if char == "." or char.isdigit():
        current += char
    else:
        if current:
            result.append(current)
            current = ""

if current:
    result.append(current)

print(result)