
def open(number,name,type,balance=0):
    return number,name,type,balance

def deposite(balance):
        n=int(input("enter the amount deposited :"))
        

        if n>=2000:
            balance=balance+n
            print("success")
        else:
            print("found")
       
        return balance



def withdrawal(balance):
    w=int(input("enter the withdrawl amount :"))
    if w <= balance:
           balance=balance-w
           print("success")
    else:
           print("not found")
    return balance

def statement(data):
    print("account number :",data[0])
    print("holder name :",data[1])
    print("account type :",data[2])
    print("account balance :",data[3])


number=int(input("enter the account number :"))
name=(input("enter the holder name :"))
type=(input("enter the account  type :"))

data=open(number,name,type)
balance=data[3]
balance = deposite(balance)
balance = withdrawal(balance)
data = (data[0], data[1], data[2], balance)
statement(data)

            

    


