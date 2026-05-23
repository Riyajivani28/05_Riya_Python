for i in range(5,0,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()


n=1
for i in range(1,6):
    for j in range(i):
        print(n,end=" ")
        n=n+1
    print()


for i in range(1,7):
    for j in range(i):
        print(chr(97+j),end=" ")
    print()