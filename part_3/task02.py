frequency = {}

with open('./files/data.txt', 'r') as f:
    for line in f:
        num = int(line.strip())
        frequency[num] = frequency.get(num, 0) + 1

for num, freq in frequency.items():
    print(f"{num} - {freq}")