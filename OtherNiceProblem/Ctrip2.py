import math
p = [1,2,3,1,2,1,3,1,3,4,1,2,3,1,3,4,1,2,3,1,2,1,2]
q = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4]

dic_p = {}
dic_q = {}
for each in p:
    if each not in dic_p:
        dic_p[each] = 1
    else:
        dic_p[each] += 1
for each in q:
    if each not in dic_q:
        dic_q[each] = 1
    else:
        dic_q[each] += 1
xset = set(p)
res = 0
for each in xset:
    res += dic_p[each]/len(p)*math.log(dic_p[each]/len(p)/(),2)