'''
小朋友平均分玩具
'''
m = 4
n = [7,15,9,5]
# n = list(map(int,n))
if divmod(sum(n),m)[1] != 0:
    print(-1)
else:
    avg = sum(n) / m
    action = 0
    for each in n:
        if each > avg:
                if divmod(each-avg,2)[1] != 0:

                    print(-1)

                    break
                action += (each - avg) / 2
    print(round(action))
