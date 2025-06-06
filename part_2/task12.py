string = str(input("-->")).split()
longest_word = ""
for word in string:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)
