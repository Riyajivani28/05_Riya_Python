try:
    price=int(input("enter price : "))
    quantity=int(input("enter quantity :"))
    total=price*quantity
    print("total amount :",total)
except ValueError:
    print("Error! please enter numeric value")
