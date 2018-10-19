# n = 5
# weapon = [1,10,100,95,101]
# c = 4
# custom = [[1,3],[2,4],[2,5],[3,5]]

n = int(input())
weapon = list(map(int,input().strip().split()))
c = int(input())
custom = []
for i in range(c):
    line = list(map(int,input().strip().split()))
    custom.append(line)

res = 0
res2 = []

for each in custom:
    flag = 0
    w = sorted(weapon[each[0]-1:each[1]])
    for i in range(len(w)-2):
        if flag ==1:
            break
        for j in range(i+1,len(w)-1):
            if flag ==1:
                break
            for k in range(j+1,len(w)):
                if w[k]- w[i] >=w[j] or flag ==1:
                    break
                if w[i]+w[j] > w[k]:
                    res +=1
                    flag = 1
                    # if [w[i],w[j],w[k]] not in res2:
                    #     res2.append([w[i],w[j],w[k]])

print(res)