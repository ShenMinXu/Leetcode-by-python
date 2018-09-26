n = int(input())
f_box = [1]
f_maybe_box =[]
res = 1
for i in range(n):
    line = input().strip().split()
    line = list(map(int,line))
    f_maybe_box.append(line)
def if_f(index,tmp):
    if index+1 in tmp:
        return
    else:
        tmp.append(index + 1)
        if f_maybe_box[index][0] == 1:
            if f_maybe_box[index][1] in f_box:
                for each in tmp:
                    if each not in f_box:
                        f_box.append(each)
            else:
                if_f(f_maybe_box[index][1]-1,tmp)


for i in range(len(f_maybe_box)):
    if_f(i,[])

print(f_box)
print("0 "+str(len(f_box)))
