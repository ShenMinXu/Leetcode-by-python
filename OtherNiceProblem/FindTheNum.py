'''
给一个数组，一个数出现一次，其它数出现两次，找出出现一次的那个数，要求：时间O(N)，空间O(1)
'''

data = [1,1,2,2,3,3,4,4,5,6]
res = data[0]
for i in range(1,len(data)):
    res = data[i] ^ res
print(res)