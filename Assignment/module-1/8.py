age=int(input("enter the age : "))
weight=int(input("enter the weight :"))
if age>=18:
    if weight>=50:
        print("eligible to donate blood")
    else:
        print("eligible to not donate blood because less than weight 50")
else:
    print("eligible to not donate blood because less than age 18")