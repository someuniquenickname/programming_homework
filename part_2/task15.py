line = str(input("-->"))
word = str(input("-->"))

if word in line:
    print(line.count(word))
else:
    print("Слова в строке нет(")