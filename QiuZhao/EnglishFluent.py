target = 9
tree = [6,3,1,0,0,4,1,0,0,0,0,0,0,0,1]
result = []

def bfs(target,index,path,res):
    if target ==0:
        res.append(path)
        return
    if tree[index] ==0:
        return
    elif target <0:
        return
    else:
        if 2*(index+1)-1<len(tree) or index==len(tree)-1:
            bfs(target-tree[index],2*(index+1)-1,path+[tree[index]],res)
        if 2*(index+1)<len(tree) or index==len(tree)-1:
            bfs(target - tree[index], 2*(index+1), path + [tree[index]], res)
bfs(target,0,[],result)
result2 =[]
for each in result:
    if each not in result2:
        result2.append(each)
print(result2)
for each in result2:
    each = list(map(str,each))
    print(' '.join(each))

a = [1,2,3]
a.insert(1,5)
print(a)