set={'riya','gatu'}
print(set)

print(len(set))

if 'riya' in set:
    print("yes..")
else:
    print("no..")

for i in set:
    print(i)

x=set.add('datii')
print(set)

set.remove('datii')
print(set)

set.update(["bhavu","datii"])
print(set)

set.add("bhavu")
print(set)