n = 10
k = 2
x = '1001010101'
res = 0
for i in range(len(x)):
    tmp = k
    tmp_res = 0
    j = i
    if len(x)-i<res:
        break
    while j<len(x):
        if int(x[j]) > 0:
            tmp_res += 1
            j+=1
        elif tmp>0:
            tmp_res +=1
            tmp -= 1
            j+=1
        else:
            break
    res = max(tmp_res,res)

print(res)
