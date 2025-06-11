with open("part_3/files/fio.txt", "r") as file:
    tmp = [ name.split() for name in file.read().lower().strip().split("\n")]





with open("part_3/files/fio2.txt", "w") as file2:
    file2.write(selection_sort(tmp))
