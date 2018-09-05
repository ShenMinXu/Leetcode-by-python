x = 'a11b2bac3bad3abcd2'
help = {}
i= 0
while i< len(x):
    tmp = ''
    while i < len(x) and x[i].isalpha():
        tmp += x[i]
        i+=1
    j = i
    while j <len(x) and x[j].isdigit() :
        j +=1
    if j>i:
        num = int(x[i:j])
    else:
        num = int(x[j])
    if tmp not in help:
        help[tmp] = num
    else:
        help[tmp] += num
    i += j-i

help2 = []
for each in help:
    help2.append((help[each],each))
help2.sort()


res =''
i = 0

while i <len(help2):
    tmp = []
    tmp.append((sum([ord(each) for each in help2[i][1]]),help2[i][1],help2[i][0]))
    while i+1<len(help2) and help2[i][0] == help2[i+1][0]:
        tmp.append((sum([ord(each) for each in help2[i+1][1]]),help2[i+1][1], help2[i+1][0]))
        i+=1
    print(tmp)
    tmp.sort()

    for each in tmp:
        res += each[1]*each[2]
    i+=1

print(res)
a = [(1,'b',3),(1,'a',4),(1,'a',3)]
a.sort()
print(a)
