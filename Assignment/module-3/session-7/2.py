class Payment:
    def pay(self, amount):
        print("Paying amount:", amount)

class UPI(Payment):
    def pay(self, amount):
        print("Paying amount via UPI:", amount)
amount = float(input("Enter amount to pay: "))
payment_obj = Payment()
upi_obj = UPI()
payment_obj.pay(amount)
upi_obj.pay(amount)