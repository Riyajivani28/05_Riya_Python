
class InvalidcouponcodeError(Exception):
    pass

valid_codes = ['RIYA10', 'save11', 'Swam1111']

coupon = input("Enter coupon code: ")

try:
    if coupon in valid_codes:
        print("Coupon code applied successfully.")
    else:
        raise InvalidcouponcodeError("Invalid Coupon Code")

except InvalidcouponcodeError as e:
    print(e)