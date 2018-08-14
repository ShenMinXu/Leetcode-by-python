#coding=utf-8
def greedy(s,f,n):
    a = [True for x in range(n)]
    #初始选择第一个活动
    j = 0
    for i in range(1,n):
        #如果下一个活动的开始时间大于等于上个活动的结束时间
        if s[i] >= f[j]:
            a[i] = True
            j = i
        else:
            a[i] = False
    return a

n = 3
m = 10
arr = input()
arr = arr.split()
s = []
f = []
for i in range(len(arr)):
    if(i % 2 == 0):
          s.append(int(arr[i]))
    else:
          f.append(int(arr[i]))

s,f = bubble_sort(s,f)
A = greedy(s,f,n)
res = []
res = 0
for k in range(len(A)):
    if A[k] and int(f[k]) <= m:
        res +=1
print(res)
