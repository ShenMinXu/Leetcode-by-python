import sys

line = input().strip().split()
n = int(line[0])
m = int(line[1])
res = [0 for i in range(n)]
for j in range(m):
    res[j] = 1

for i in range(1, n):
    tmp = i - 1
    flag = m
    while m > 0 and tmp >= 0:
        res[i] += res[tmp]
        flag -= 1
        tmp -= 1

print(res[-1])

