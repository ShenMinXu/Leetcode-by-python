n  = 5
mat = [[1,0,0,1,1],[1,0,0,1,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]]
res = 0
def change1to0(i,j):
    if i<len(mat) and j< len(mat[0]) and i>=0 and j>=0:
        if mat[i][j] > 0:
            mat[i][j] = 0
            change1to0(i-1,j)
            change1to0(i+1,j)
            change1to0(i,j-1)
            change1to0(i,j+1)
    return None


# for i in range(n):
#     line = input().split()
#     mat.append(line)

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] > 0:
            res += 1
            change1to0(i,j)
print(res)
