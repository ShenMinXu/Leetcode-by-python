import math
x = 7
y = 14
k = int(math.sqrt(2*(x+y)))
score = [i for i in range(1,k+1)]

n =  0
def help():
    tmp = x
    res = 0
    for i in range(len(score)-1,-1,-1):
        if tmp > 0:
            if tmp >= score[i]:
                tmp -= score[i]
                res += 1
        if tmp ==0:
            return res
        if tmp <0:
            break
    return -1

res = help()
print(res)
