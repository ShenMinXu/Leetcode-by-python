import string

x1 = ''
x2 = ''
num_to_abc = {}
abc_to_num = {}
i = 0
for word in string.ascii_lowercase:
    num_to_abc[i] = word
    abc_to_num[word] = i
    i+=1

def cal(shorter,longer):
    res= ''
    add_num = 0
    shorter = shorter[::-1]
    longer = longer[::-1]
    for i in range(len(longer)):
        if i < len(shorter):
            tmp = abc_to_num[shorter[i]]+abc_to_num[longer[i]] + add_num
            add_num = tmp // 26
            tmp = tmp % 26
            res += num_to_abc[tmp]
        else:
            tmp = abc_to_num[longer[i]] + add_num
            add_num = 0
            res += num_to_abc[tmp]
    if add_num >0:
        res += num_to_abc[add_num]
    return res[::-1]

len_x1 = len(x1)
len_x2 = len(x2)
if len_x1 >= len_x2:
    res = cal(x2,x1)
else:
    res  =cal(x1,x2)

print(res)

