s1=int(input("enter asp mark :"))
s2=int(input("enter java mark :"))
s3=int(input("enter php mark :" ))
s4=int(input("enter python mark :" ))


total=(s1+s2+s3+s4)
print(total)
per=(s1+s2+s3+s4)/4
print(per)

if per>=90:
    print("A")
elif per>=70:
    print("B")
elif per>=50:
    print("c")
else:
    print("D")