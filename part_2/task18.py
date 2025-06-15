line = input("-->")
alphabet = {}
for char in line:
    alphabet[char] = alphabet.get(char, 0) + 1
print(alphabet)