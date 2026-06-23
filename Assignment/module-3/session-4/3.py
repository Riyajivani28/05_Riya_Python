class PaymentFailedError(Exception):
    pass

def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError("Payment Failed")
    
    print("Payment Successful")

try:
    amount = int(input("Enter payment amount: "))
    process_payment(amount)

except PaymentFailedError as e:
    print(e)