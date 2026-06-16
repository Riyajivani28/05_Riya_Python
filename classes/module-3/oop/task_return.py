class open:
    def o_display(self):
        self.num = int(input("Enter Acc Number : "))
        self.name = input("Enter Acc Name : ")
        self.type = input("Enter Acc Type : ")
        self.balance = 0


class deposite(open):
    def depo(self):
        n = int(input("Enter Deposit : "))

        if n >= 2000:
            self.balance += n
            return True
        else:
            print("Deposit must be 2000")
            return False


class withdraw(deposite):
    def draw(self):
        n1 = int(input("Enter Withdrawal : "))

        if n1 <= self.balance:
            self.balance -= n1
            return "Withdrawal Success"
        else:
            return "Insufficient Balance"


class statement(withdraw):
    def show(self):
        return f"""
-------ACCOUNT STATEMENT----------
Acc Number : {self.num}
Acc Name   : {self.name}
Acc Type   : {self.type}
Balance    : {self.balance}
"""


s = statement()
s.o_display()

print(s.depo())
print(s.draw())
print(s.show())