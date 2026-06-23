import re

text = input("Enter text with mobile number: ")

pattern = r'\b\d{10}\b'

match = re.search(pattern, text)

if match:
    print("First mobile number found:", match.group())
else:
    print("No valid 10-digit mobile number found")