import re

mystr="My name is Riya JIvani 1234567890"

#x=re.findall('^My',mystr)
#x=re.findall('^[A-Z]',mystr)
x=re.findall("90$",mystr)
print(x)