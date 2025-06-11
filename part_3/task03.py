with open("part_3/files/fio.txt", "r") as file:
    tmp = [ name.split() for name in file.read().lower().strip().split("\n")]


def quicksearch(left, right, tmp):
    if (right - left) > 1:
        mid = (right + left) //2
        quicksearch(left, mid, tmp)
        quicksearch(mid+1, right, tmp)
    return 0

quicksearch(0, len(tmp), tmp)
print(tmp)
# with open("part_3/files/fio2.txt", "w") as file2:
#     file2.write("\n".join(tmp))

