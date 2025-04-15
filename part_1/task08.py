x1, y1, x2, y2, z2 =  map(int, input("размеры дыры и кирпича (ax ay bx by bz ):--->").split())
eggs = sorted([x2, y2, z2])
if (x1 >= eggs[0] and y1 >= eggs[1]) or (y1 >= eggs[0] and x1 >= eggs[1]):
    print("Влезает!")
else:
    print("Не лезет!")
