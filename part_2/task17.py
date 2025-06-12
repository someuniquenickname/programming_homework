line = str(input("-->"))

words = line.split()
line = " ".join(words)

punctuation = ['.', ',', '?', '!', ':', ';']
newLine = ""
lastSymbolWasPun = False

for symbol in line:
    if symbol in punctuation:
        if not lastSymbolWasPun:
            newLine = newLine.rstrip()  # Remove trailing space before punctuation
            newLine += symbol
            lastSymbolWasPun = True
    else:
        newLine += symbol
        lastSymbolWasPun = False
line = newLine

line = line.replace("( ", "(").replace(" )", ")")

print(line)