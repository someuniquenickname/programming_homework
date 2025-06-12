line = str(input("-->"))

alphabet = {}

for i in line:
    if i in alphabet:
        alphabet[i] += 1
    else:
        alphabet[i] = 1
    
print(alphabet)