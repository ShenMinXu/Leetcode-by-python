num = 3
corpus= []
corpus2 =[]
input = [
[1,10],[32,45],
[78,94],[5,16],
[80,100],[200,220],[16,32]]

input2  = '1,10;32,45;78,94;5,16;80,100;200,220;16,32'

for _ in range(1):
    line = input2.split(';')
    for each in line:
        each =each.split(',')
        corpus.append((int(each[0]),int(each[1])))

corpus.sort()

res = [corpus[0][0],corpus[0][1]]
for i in range(1,len(corpus)):
    if corpus[i][0] <= res[1]:
        res[1] = max(corpus[i][1],res[1])
    else:
        print(str(res[0])+','+str(res[1]),end=';')
        res = [corpus[i][0],corpus[i][1]]
print(str(res[0])+','+str(res[1]))






