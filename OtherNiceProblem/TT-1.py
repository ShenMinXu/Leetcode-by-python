m  =10
n = 10
c = [
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,1,0,0,0],
[0,1,0,0,0,0,0,1,0,1],
[1,0,0,0,0,0,0,0,1,1],
[0,0,0,1,1,1,0,0,0,1],
[0,0,0,0,0,0,1,0,1,1],
[0,1,1,0,0,0,0,0,0,0],
[0,0,0,1,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0]]
g = 0
maxgnum = 0

def help2(i,j):
    return help1(i-1,j-1)+help1(i-1,j)+help1(i-1,j+1)+help1(i,j-1)+help1(i,j+1)+help1(i+1,j-1)+help1(i+1,j)+help1(i+1,j+1)

def help1(i,j):
    if i >=0 and i<m and j>=0 and j<n:
        if c[i][j] == 1:
            c[i][j] = 0
            return 1 + help2(i,j)

        else:
            return 0
    else:
        return 0

for i in range(len(c)):
    for j in range(len(c[0])):
        if c[i][j] == 1:
            g +=1
            maxgnum = max(maxgnum,help2(i,j))

print(str(g)+' '+str(maxgnum))
