'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''
for i in range(6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()