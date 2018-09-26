n = int(input())
line = input().strip().split()
stone = list(map(int,line))
max__self_attack = 0
def get_attack(index):
    res = 0
    for i in range(index):
        if stone[i] >stone[index]:
            res += 1
    for i in range(index+1,len(stone)):
        if stone[i] < stone[index]:
            res +=1
    return res

max_reduce = 0
max_reduce_index = 0
all_attack = 0
for i in range(len(stone)):
    tmp = get_attack(i)
    if i <= tmp and tmp - i>max_reduce:
        max_reduce = tmp-i
        max_reduce_index = i

for i in range(len(stone)):
    for j in range(i+1,len(stone)):
        if stone[i] > stone[j]:
            all_attack +=1

print(all_attack-max_reduce)
print(max_reduce_index+1,end=" ")


