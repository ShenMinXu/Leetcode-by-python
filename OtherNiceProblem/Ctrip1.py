import numpy as np
import math
n = 5
x = [1,1,2,0,3]
y = [1,1,0,0,0]
def help(list_in):
    p1 = sum(list_in)/len(list_in)
    if p1 == 0 or p1== 1:
        return 0
    p2 = 1 - p1
    S = -1*(p1*math.log(p1,2)+p2*math.log(p2,2))
    return S


feature = {}
for i in range(n):
    if x[i] not in feature:
        feature[x[i]]  = [y[i]]
    else:
        feature[x[i]].append(y[i])

res = help(y)
for each in feature:
    res -= len(feature[each])/len(y)*help(feature[each])
print(round(res,2))


