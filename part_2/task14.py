pairs = {"(": ")", "{": "}", "[": "]"}
stack = []
s = input("Строка : ")
balanced = True

for char in s:
    if char in pairs:
        stack.append(char)
    elif char in pairs.values():
        if not stack or pairs[stack.pop()] != char:
            balanced = False
            break

print("Всё верно" if balanced and not stack else "Ошибка")