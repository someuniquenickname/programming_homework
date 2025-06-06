import math
n = int(input("-->"))

res = 1

for i in range(1,n+1):
    res*=i

print(pow(res, 1/n))