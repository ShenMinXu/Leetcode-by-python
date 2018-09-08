
n = int(input())
mat = []
for i in range(n):
    a = []
    s = input()
    if s != "":
        for x in s.split(','):
            a.append(int(x))
        mat.append(a)
    else:
        break

for i in range(1,n):
    mat[0][i] += mat[0][i-1]
    mat[i][0] += mat[i-1][0]

for i in range(1,n):
    for j in range(1,n):
        mat[i][j] += min(mat[i-1][j],mat[i][j-1])

print(mat[n-1][n-1])