import math
x = 2
y = 3
z = 3
res = 0
for eachx in range(1,x+1):
    for eachy in range(1,y+1):
        for eachz in range(1,z+1):
            tmp = [eachx,eachy,eachz]
            tmp.sort()
            if tmp[0]+tmp[1]>tmp[2] and tmp[2]-tmp[1]<tmp[0]:
                res+=1
print(divmod(res,1000000007)[1])
