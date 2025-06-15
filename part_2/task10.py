line = input("-->")
for punct in ",.:;-!?":
    line = line.replace(punct, " ")
print(len(line.split()))