import re

order_ids = ['ORD1234', 'ORD5678', 'ORD9999', 'ORD0001']
pattern = r'^ORD\d*[02468]$'
for order in order_ids:
    if re.match(pattern, order):
        print(order)