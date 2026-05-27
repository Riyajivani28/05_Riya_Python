data=[]
n=int(input("how many want the student detail :"))
for i in range(n):
    dict={}
    p=int(input("how many pair in the student :"))
    for j in range(p):
        key=input("enter the key name :")
        value=input("enter the value name :")
        dict[key]=value
    data.append(dict)
print(data)