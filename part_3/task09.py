substring = input("Введите подстроку: ")
filename = input("Введите имя файла: ")

with open(filename, 'r') as f:
    for line_num, line in enumerate(f, 1):
        if substring in line:
            print(f"Строка {line_num}: {line.strip()}")