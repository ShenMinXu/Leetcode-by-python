n = 3
if n<4:
    print(n)
else:
    tmp = divmod(n,4)
    left = tmp[0]
    bit_4 = tmp[1]
    res = []
    while left > 3:
        res.append(bit_4)
        tmp = divmod(left,4)
        left = tmp[0]
        bit_4 = tmp[1]
    res.append(bit_4)
    res.append(left)
    res = list(map(str,res))
    print(''.join(res[::-1]))