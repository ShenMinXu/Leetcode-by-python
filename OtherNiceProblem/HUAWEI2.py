input1 = 'BBDDCFFE'
input2 = 'LCEFB'

set_input2 = set(input2)
for each in set_input2:
    if each not in input1:
        print('true')
    break
print('false')
