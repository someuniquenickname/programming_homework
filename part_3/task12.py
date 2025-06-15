import os

def quicksort(arr, key=None, reverse=False, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high, key, reverse)
        quicksort(arr, key, reverse, low, pi - 1)
        quicksort(arr, key, reverse, pi + 1, high)
    
    return arr

def partition(arr, low, high, key, reverse):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if key:
            condition = (key(arr[j]) <= key(pivot)) != reverse
        else:
            condition = (arr[j] <= pivot) != reverse
            
        if condition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

files = [(f, os.path.getsize(f)) for f in os.listdir('.') if os.path.isfile(f)]
sorted_files = quicksort(files, key=lambda x: x[1], reverse=True)

for filename, size in sorted_files:
    print(f"{filename}: {size} bytes")