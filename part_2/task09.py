while True:
    try:
        line = input("-->")
        result = len(line.split())
        break
    except:
        print("Невалидная строка")
print(f"Кол-во слов в этой строке равно {result}")



