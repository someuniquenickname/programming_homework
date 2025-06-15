nums1 = []
nums2 = []

with open('./files/data1.txt', 'r') as f:
    nums1 = [int(line.strip()) for line in f]

with open('./files/data2.txt', 'r') as f:
    nums2 = [int(line.strip()) for line in f]

merged = []
i, j = 0, 0

while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        merged.append(nums1[i])
        i += 1
    else:
        merged.append(nums2[j])
        j += 1

merged.extend(nums1[i:])
merged.extend(nums2[j:])

with open('./files/merged.txt', 'w') as f:
    for num in merged:
        f.write(str(num) + '\n')