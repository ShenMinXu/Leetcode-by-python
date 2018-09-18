import re
a = '12345abc'
b =re.findall('[0-9]{5}',a,re.S)
print(b)