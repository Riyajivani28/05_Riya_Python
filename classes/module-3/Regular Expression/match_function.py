import re

x="hello everyone!"
'''y=re.match("everyone",x)#output (none) bcz only begging word'''
y=re.match("hello",x)
print(y)

if y:
    print("DONE")
else:
    print("ERROR")