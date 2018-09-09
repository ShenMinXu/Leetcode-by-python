'''
判断是否为二分图
'''
m = 5
n = 7
spots = [1,2,2,3,3,4,4,1,4,5,5,2]
graph = {}
colour = {}
i = 0
while i < len(spots):
    if spots[i] not in graph:
        graph[i] = [graph[i+1]]
    else:
        graph[i].append(graph[i+1])
    if spots[i+1] not in graph:
        graph[i+1] = [graph[i]]
    else:
        graph[i+1].append(graph[i])
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
    res1 = help(each,colour,1)
    res2 = help(each,colour,0)
    res = res1 and res2
    if not res:
        print('False')
    break