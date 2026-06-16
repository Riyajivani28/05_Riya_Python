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
            print("Deposit Success")
        else:
            print("Deposit must be 2000")
            


class withdraw(deposite):
    def draw(self):
        n1 = int(input("Enter Withdrawal : "))

        if n1 <= self.balance:
            self.balance -= n1
            print("Withdrawal Success")
        else:
            print("Insufficient Balance")


class statement(withdraw):
    def show(self):
        print("\n-------ACCOUNT STATEMENT----------")
        print("Acc Number :", self.num)
        print("Acc Name :", self.name)
        print("Acc Type :", self.type)
        print("Balance :", self.balance)


s = statement()
s.o_display()
s.depo()
s.draw()
s.show()