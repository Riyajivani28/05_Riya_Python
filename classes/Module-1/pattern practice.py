for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print("******************************")

for i in range(1,6):
    for j in range(1,6):
        if i==3 and j==3:
            print("$",end=" ")
        else:
            print("*",end=" ")
       
    print()

print("******************************")
n=1
for i in range(1,6):
    for j in range(i):
        print(n,end=" ")
        n=n+1
    print()
print("******************************")
n=0
for i in range(6):
    for j in range(1,6):
        print(chr(65+n),end=" ")
        n=n+1
    print()
print("******************************")

