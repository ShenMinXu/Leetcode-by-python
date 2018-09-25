num = input()
n = int(num.split()[0])
m = int(num.split()[1])
count = m
list_do = []
while count > 0:
    tmp = int(input())
    list_do.append(tmp)
    count -= 1
nums = [j+1 for j in range(n)]
res =[]
for i in range(len(list_do)-1,-1,-1):
    if list_do[i] not in res:
        res.append(list_do[i])
res = res + [each for each in nums if each not in res]
print(res)