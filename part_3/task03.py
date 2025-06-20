def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

with open('./files/fio.txt', 'r') as f:
    names = [line.strip() for line in f if line.strip()]

sorted_names = quicksort(names)

with open('./files/fio2.txt', 'w') as f2:
    for name in sorted_names:
        f2.write(name + '\n')