n  = int(input())
res = [0 for i in range(n)]
res[0] = 2
res[1] = 3
for i in range(2,n):
    res[i] = res[i-1]+res[i-2]
print(res[-1])