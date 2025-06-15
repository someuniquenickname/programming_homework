filename = input("Введите имя файла: ")
char_count = {}
total_chars = 0
whitespace_chars = 0

with open(filename, 'r') as file:
    for line in file:
        for char in line:
            total_chars += 1
            char_count[char] = char_count.get(char, 0) + 1
            if char in ' \t\r\n':
                whitespace_chars += 1

for char, count in char_count.items():
    print(f"'{char}': {count}")

whitespace_percent = (whitespace_chars / total_chars) * 100 if total_chars > 0 else 0
print(f"Процент пробельных символов: {whitespace_percent:.2f}%")