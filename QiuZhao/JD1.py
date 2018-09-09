
s = 'ababcb'
t = 'xyx'


def solve(S,T):
    s_dic = {}
    t_dic = {}
    if len(S) != len(T):
        return 0
    path_S = []
    path_T = []
    for i in range(len(S)):
        j = i
        count_s = 1
        if S[i] not in s_dic:
            s_dic[S[i]] = len(s_dic)
        while j+1 < len(S) and S[j+1]==S[j]:
            count_s += 1
            j+=1
        if j > i:
            i = j-1
        path_S.append((s_dic[S[i]],count_s))

    for i in range(len(T)):
        j = i
        count_t = 1
        if T[i] not in t_dic:
            t_dic[T[i]] = len(t_dic)
        while j+1 <len(T) and T[j+1]==T[j]:
            count_t += 1
            j+=1
        if j > i :
            i = j -1
        path_T.append((t_dic[T[i]],count_t))

    for i in range(len(S)):
        if path_T[i] != path_S[i]:
            return 0
    return 1


len_t = len(t)
len_s = len(s)
res = 0
if len_s >= len_t:
    for i in range(len(s)-len(t)+1):
        # print(s[i:i+3])
        res += solve(s[i:i+len(t)],t)
    print(res)
else:
    for i in range(len(t) - len(s) + 1):
        # print(s[i:i+3])
        res += solve(t[i:i+len(s)], s)
    print(res)

