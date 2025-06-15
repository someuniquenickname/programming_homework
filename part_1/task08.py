x1, y1, x2, y2, z2 = map(int, input("размеры дыры и кирпича (ax ay bx by bz ):--->").split())
brick = sorted([x2, y2, z2])
if (x1 >= brick[0] and y1 >= brick[1]) or (x1 >= brick[1] and y1 >= brick[0]):
    print("Влезает!")
else:
    print("Не лезет!")