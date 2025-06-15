import re

filename = input("Введите имя файла: ")
word_count = {}

with open(filename, 'r') as f:
    text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

with open('./files/word.csv', 'w', encoding='utf-8') as f:
    for word, count in word_count.items():
        f.write(f"{word},{count}\n")