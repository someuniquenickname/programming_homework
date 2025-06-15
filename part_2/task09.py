try:
    line = input("-->")
    print(f"Кол-во слов в этой строке равно {len(line.split())}")
except:
    print("Невалидная строка")