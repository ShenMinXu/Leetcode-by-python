n = 5
m = 20
tree = [11,11]
# line = input().strip().split()
# n = int(line[0])
# m = int(line[1])
# line = input().strip().split()
# tree = list(map(int,line))
tree.sort()
up = max(tree)
low = 0
mid = low+(up-low)//2
res = 0
def help(target,index,tree):
    target = target - tree[index]
    if target == 0:
        return 1
    else:
        for i in range(index+1,len(tree)):
            tmpres = help(target,i,tree)
            if tmpres:
                return 1
    return 0
# aa = help(20,0,[4,6,10])
# print('**')
# print(aa)

while mid < up:
    tmptree = [each-mid for each in tree if each>mid]
    print(mid)
    print(tmptree)
    tmpsum = sum(tmptree)
    tmpres = help(m,0,tmptree)
    # print(tmpres)
    if tmpsum == m:
        res = max(res,mid)
        low = mid + 1
        mid = low + (up - low) // 2
    if  tmpsum > m:
        low = mid + 1
        mid = low + (up -low)//2
    if tmpsum < m:
        up = mid
        mid = low + (up -low)//2
print(res)

