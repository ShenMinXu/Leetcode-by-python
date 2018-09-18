q = int(input())
q_s=[]
for i in range(q):
    line = input().strip().split()
    line = list(map(int,line))
    q_s.append(line)
for each in q_s:
    k  = each[0]
    l  = each[1]
    r  = each[2]
    n = 0
    if k-1 <l or  k-1 >r:
        print('None')
    else:
        tmp = (k-1)*(k)**n
        while tmp<=r:
            n +=1
            tmp += (k-1)*(k**n)
        tmp = tmp -(k-1)*(k)**n
        print(tmp)


