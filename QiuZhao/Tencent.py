a = 'abab'
b ='ababab'
k = 2
d_a = {}
count = 0
for i in range(len(a)-k+1):
    tmp = a[i:i+k]
    d_a[tmp] = 1
for i in range(len(b)-k+1):
    tmp =b[i:i+k]
    if tmp  in d_a:
        count +=1
print(count)