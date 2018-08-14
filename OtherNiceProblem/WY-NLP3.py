n = 3
k =2
h0 = [5,8,5]
h_min = 10**4+1
h_max = 0
h_dic = {}
res_num = 0
for each in h0:
    if each < h_min:
        h_min = each
    if each > h_max:
        h_max = each
    if each in h_dic:
        h_dic[each] = h_dic[each] + 1
    else:
        h_dic[each] =1

h = h_max - h_min
while h>0 and k>0:
    h_dic[h_max] -= 1
    h_dic[h_min] -= 1
    if h_max-1 in h_dic:
        h_dic[h_max-1] += 1
    else:
        h_dic[h_max-1] = 1

    if h_min+1 in h_dic:
        h_dic[h_min+1] += 1
    else:
        h_dic[h_min+1] = 1


    if h_dic[h_max] == 0:
        h_max -= 1
    if h_dic[h_min] == 0:
        h_min += 1
    h = h_max - h_min
    res_num += 1
print(str(h)+' '+str(res_num))







