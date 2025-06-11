dict = {"(":")", "{":"}", "[":"]"}
stack = []
s = input("Строка : ")
balanced = True
for i in range(len(s)):
    if s[i] in dict:
        stack.append(s[i])
    elif s[i] == ')' or s[i] == '}' or s[i] == ']':
        if dict[stack[len(stack) - 1]] == s[i]:
            stack.pop()
        else:
            balanced = False
            break

if balanced == True:
    print("Всё верно")
else:
    print("Ошибка")