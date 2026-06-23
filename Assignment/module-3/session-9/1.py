import re
email = input("Enter Gmail address: ")
pattern = r'^[a-z][a-z0-9._%+-]*@gmail\.com$'
if re.match(pattern, email):
    print("Valid Gmail")
else:
    print("Invalid Gmail")