fruit=["apple","banana","cherry"]
print(fruit)
print(fruit[0])
print(fruit[-1])
fruit.insert(2,"pinapple")
print(fruit)

for i in fruit:
    print(i)

if "banana" in fruit:
    print("yes")
else:
    print("no")

fruit.append("coconut")
print(fruit)

fruit.reverse()
print(fruit)

f1=fruit.copy()
print(f1)

f1.remove("apple")
print(f1)


f2=["riya","gatu"]
print(f2)
