class open:
    def o_display(self):
        global balance
        self.num = int(input("Enter Acc Number : "))
        self.name = input("Enter Acc Name : ")
        self.type = input("Enter Acc Type : ")
        balance = 0


class deposite(open):
    def depo(self):
        global balance

        n = int(input("Enter Deposit : "))

        if n >= 2000:
            balance += n
            print("Deposit Success")
            return True
        else:
            print("Deposit must be 2000")
            return False


class withdraw(deposite):
    def draw(self):
        global balance

        n1 = int(input("Enter Withdrawal : "))

        if n1 <= balance:
            balance -= n1
            print("Withdrawal Success")
        else:
            print("Insufficient Balance")


class statement(withdraw):
    def show(self):
        global balance

        print("\n-------ACCOUNT STATEMENT----------")
        print("Acc Number :", self.num)
        print("Acc Name :", self.name)
        print("Acc Type :", self.type)
        print("Balance :", balance)


s = statement()
s.o_display()

if s.depo():
    s.draw()
    s.show()