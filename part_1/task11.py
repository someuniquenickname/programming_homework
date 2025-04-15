print("\n".join(([(" "*(x) + "*" + ((4-x)*2-1)*" " + ("*" if (x != 4 and x != 0) else "") + " "*(x*2 - 1) + "*" + ((4-x)*2-1)*" " + ("*" if (x != 4) else "")) for x in range(5)])))

