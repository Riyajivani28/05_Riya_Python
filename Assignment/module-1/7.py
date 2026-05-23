s1=int(input("enter python mark : "))
s2=int(input("enter php mark : "))
s3=int(input("enter java mark :"))

total=s1+s2+s3
print("Result total : ",total)

pr=total/3
print("Result PR :",pr)

if s1>40 and s2>40 and s3>40:
    if pr>=80:
        print("Result Grade : A")
    elif pr>=60:
        print("Result Grade : B")
    elif pr>=50:
        print("Result Grade : C")
else:
    print("fail")