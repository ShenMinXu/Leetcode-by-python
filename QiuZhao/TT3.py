'''
复原IP地址
回溯法
'''
s =input()
res =[]
def help(s, index, path):
    if index == 4:
        if not s:
            res.append(path[:-1])
        return
    for i in range(1, 4):

        if i <= len(s):

            if i == 1:
                help(s[i:], index + 1, path + s[:i] + ".")

            elif i == 2 and s[0] != "0":
                help(s[i:], index + 1, path + s[:i] + ".")

            elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                help(s[i:], index + 1, path + s[:i] + ".")
help(s,0,'')
print(len(res))



