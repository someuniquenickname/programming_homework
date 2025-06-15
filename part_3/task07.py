import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

n = int(input("Введите N (>100): "))
numbers = [random.randint(1, 30) for _ in range(n)]
sorted_numbers = quicksort(numbers)

with open('./files/data1.txt', 'w') as f:
    for i in range(0, len(sorted_numbers), 2):
        f.write(str(sorted_numbers[i]) + '\n')

with open('./files/data2.txt', 'w') as f:
    for i in range(1, len(sorted_numbers), 2):
        f.write(str(sorted_numbers[i]) + '\n')