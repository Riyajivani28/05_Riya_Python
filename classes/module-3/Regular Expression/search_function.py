import re

str="Hello! I am Riya Jivani.."
x=re.search("I",str)
print(x)

if x:
    print("DONE")
else:
    print("ERROR")