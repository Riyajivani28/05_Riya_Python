f = open("orders.txt", "r")

line = f.readline()
while line:
    print("Order:", line.strip())
    print("Position:", f.tell())
    line = f.readline()
