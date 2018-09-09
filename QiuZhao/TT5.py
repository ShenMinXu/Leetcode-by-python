'''
头条网红题
'''
n = 3
m = 3
line = [1,2,2,1,2,3]
pairs = []
i = 0
dic_user1_like_user2 = {}
dic_user2_like_user1 = {}
res =0
while i <len(line):
    pairs.append((line[i],line[i+1]))
    i += 2

for user1,user2 in pairs:
    if user2 not in dic_user1_like_user2:
        dic_user1_like_user2[user2] = [user1,user2]
    else:
        dic_user1_like_user2[user2].append(user1)

print(dic_user1_like_user2)

def get_fensi(user,fensi):
    if user in dic_user1_like_user2:
        for each in dic_user1_like_user2[user]:
            if each not in fensi:
                fensi.append(each)
                # print(fensi)
                if each in dic_user1_like_user2:
                    fensi = get_fensi(each,fensi)
    return fensi

for each in dic_user1_like_user2:
    all_fensi = get_fensi(each,[])
    print(all_fensi)
    if len(all_fensi) == n:
        res+=1
print(res)




