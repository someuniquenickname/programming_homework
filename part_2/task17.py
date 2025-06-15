line = input("-->")
words = line.split()
line = " ".join(words)

punctuation = '.,:;!?'
result = ""
i = 0

while i < len(line):
    if line[i] in punctuation:
        result = result.rstrip() + line[i]
    else:
        result += line[i]
    i += 1

result = result.replace("( ", "(").replace(" )", ")")
print(result)