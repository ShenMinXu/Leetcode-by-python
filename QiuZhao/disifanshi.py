'''
判断是否为二分图
'''
mn = input().strip().split()
n = int(mn[0])
m = int(mn[1])
spots =[]
for i in range(m-1):
    line = input().strip().split()
    if not line:
        break
    line = list(map(int,line))
    spots += line
# spots = [1,2,2,3,3,4,4,1,4,5,5,2]
graph = {}
colour = {}
i = 0
while i < len(spots):
    if spots[i] not in graph:
        graph[spots[i]] = [spots[i+1]]
    else:
        graph[spots[i]].append(spots[i+1])
    if spots[i+1] not in graph:
        graph[spots[i+1]] = [spots[i]]
    else:
        graph[spots[i+1]].append(spots[i])
    if spots[i] not in colour:
        colour[spots[i]] = 2
    if spots[i+1] not in colour:
        colour[spots[i+1]] = 2
    i += 2

def help(spot,tmp,colour_value):
    if tmp[spot] ==2:
        tmp[spot] = colour_value
        for each in graph[spot]:
            help(each,tmp,1-colour_value)
        return True
    elif tmp[spot] != colour_value:
        return False

for each in graph:
    tmp = colour.copy()
    res1 = help(each,tmp,1)
    tmp = colour.copy()
    res2 = help(each,tmp,0)
    res = res1 and res2
    if not res:
        res = 0
        break
if not res:
    print('No')
else:
    print('Yes')