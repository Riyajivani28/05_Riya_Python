'''Given the following buggy code, fix it so that it catches both IndexError 
and KeyError and prints a custom message for each:<br><br>
my_list = [1, 2, 3]
print(my_list[5])
my_dict = {'a': 1}
print(my_dict['b'])<br><br><em><strong>Hint:</strong> Use multiple
except clauses to handle each exception separately.</em>'''

try:
    list=[1,2,3]
    print(list[5])
except IndexError:
    print("index is not found")

try:
    dict={'a':1}
    print(dict['b'])
except KeyError:
    print("key not found")
