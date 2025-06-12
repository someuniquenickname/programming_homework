line = str(input("-->"))

resline = line

for i in range(len(line)):
    symbol = line[i:i+1]
    if symbol != ".":
        try:
            int(symbol)
        except ValueError:
            resline = resline[:i] + " " + resline[i+1:]



print( resline.split() )