import os

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
sorted_files = quicksort(files)

for filename in sorted_files:
    print(filename)