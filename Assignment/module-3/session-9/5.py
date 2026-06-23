import re

def is_valid_pnr(pnr):
    pattern = r'^\d{10}$'
    
    if re.match(pattern, pnr):
        return True
    else:
        return False
user_input = input("Enter PNR number: ")

if is_valid_pnr(user_input):
    print("Valid PNR")
else:
    print("Invalid PNR")
