def sum(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b

n1=int(input("enter the any number :"))
n2=int(input("enter the any number :"))
choice=input("enter sny one(+,/,*,-) :")

if choice=="+":
    print("sum :",sum(n1,n2))
elif choice=="*":
    print("mul :",mul(n1,n2))
elif choice=="-":
    print("sub :",sub(n1,n2))
elif choice=="/":
    print("div :",div(n1,n2))
else:
    print("invalid")