with open("part_3/files/fio.txt", "r") as file:
    tmp = [ name.split() for name in file.read().lower().strip().split("\n")]

def selection_sort(arr):
    for i in range(len(arr)):
        lmin = i
        for j in range(i,len(arr)):
            if arr[j][0] < arr[lmin][0]:
                lmin = j
            elif arr[j][0] == arr[lmin][0] and arr[j][1] < arr[lmin][1]:
                lmin = j
            elif arr[j][0] == arr[lmin][0] and arr[j][0] == arr[lmin][0] and arr[j][2] < arr[lmin][2]:
                lmin = j
        if lmin != i:
            arr[i], arr[lmin] = arr[lmin], arr[i]
    return "\n".join([" ".join(name) for name in arr])


with open("part_3/files/fio2.txt", "w") as file2:
    file2.write(selection_sort(tmp))
