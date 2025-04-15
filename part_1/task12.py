y = int(input("--->"))
y -= 1
print("\n".join(([(" "*(x) + "*" + ((y-x)*2-1)*" " + ("*" if (x != y and x != 0) else "") + " "*(x*2 - 1) + "*" + ((y-x)*2-1)*" " + ("*" if (x != y) else "")) for x in range(y+1)])))
