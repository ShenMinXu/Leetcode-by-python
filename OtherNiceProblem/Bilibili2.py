while True:
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    if m==-1 and n==-1:
        break
    mat = []
    for i in range(m):
        line = input().split()
        line = list(map(int, line))
        if line[0] ==-1 and line[1] ==-1:
            break
        mat.append(line)
    res =[]
    while mat:
        res +=mat.pop(0)
        if mat:
            row = len(mat)
            col = len(mat[0])
            new_mat = []
            for i in range(col):
                new_line = []
                for j in range(row):
                    new_line.append(mat[j][col-1-i])
                new_mat.append(new_line)
            mat =new_mat

    res  =list(map(str,res))
    print(','.join(res))