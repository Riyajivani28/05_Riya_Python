data = []
n = int(input("How many dictionaries : "))
for i in range(n):
    my_dict = {}
    m = int(input("How many pairs in dictionary : "))
    for j in range(m):
        key = input("Enter key : ")
        value = input("Enter value : ")
        my_dict[key] = value
    data.append(my_dict)
print(data)