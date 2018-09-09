'''
最长不重复字串
'''
s = input()
tmp  = 0
maxlen = 0
dic = {}
start =0
for i in range(len(s)):
    if s[i] in dic and dic[s[i]] >= start:
        start = dic[s[i]]+1
    tmp = i - start +1
    dic[s[i]] = i
    maxlen = max(maxlen,tmp)

print(maxlen)

