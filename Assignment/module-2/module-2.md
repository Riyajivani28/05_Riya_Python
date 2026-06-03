											Collections, functions and Modules
											
-->Accessing List:

1. Understanding how to create and access elements in a list.
- list:A list in Python is used to store multiple values in a single variable.
- creating a list:You can create a list using square brackets [].
- Lists are ordered
- Lists are mutable (can be changed)
- Lists allow duplicate values
Example:
n=[10,20,30]
p=["riya","gatu"]
m=[10,"riya"]
print(n)
print(p)
print(m)

--> Accessing List Elements:List elements are accessed using index numbers.
- Index always starts from 0.
Example:
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[0])   
print(fruits[1])   
print(fruits[2])   

-->Negative Indexing:Negative indexing starts from the end.
Example:
print(fruits[-1])   
print(fruits[-2])   

-->Taking List Input from User:
Example:
numbers = []
for i in range(3):
    n = int(input("Enter number: "))
    numbers.append(n)
print("List is:", numbers)

---------------------------------------------------------------------------------------------------------------------------------------------------

2. Indexing in lists (positive and negative indexing).
-->Indexing in Python Lists: Indexing is used to access elements from a list.
* Positive Indexing: Positive indexing starts from 0 and moves left to right.
Example:
colors = ["Red", "Green", "Blue", "Yellow"]
print(colors[0])   
print(colors[1])   
print(colors[2])   
print(colors[3])   
- Positive Index Table:
| Index | Value  |
| ----- | ------ |
| 0     | Red    |
| 1     | Green  |
| 2     | Blue   |
| 3     | Yellow |

*Negative Indexing: Negative indexing starts from -1 and moves right to left.
Example:
colors = ["Red", "Green", "Blue", "Yellow"]
print(colors[-1])
print(colors[-2])   
print(colors[-3])   
print(colors[-4]) 
-Negative Index Table:
| Index | Value  |
| ----- | ------ |
| -1    | Yellow |
| -2    | Blue   |
| -3    | Green  |
| -4    | Red    |

--------------------------------------------------------------------------------------------------------------------------------------------------

3. Slicing a list: accessing a range of elements.
-->List Slicing in Python:
*Slicing is used to access a range of elements from a list.
Syntax:
python id="m0pdq0"
list_name[start : end : step]
- `start` ? Starting index
- `end` ? Ending index (not included)
- `step` ? Increment value (optional)
Example List:
numbers = [10, 20, 30, 40, 50, 60]

| Index | Value |
| ----- | ----- |
| 0     | 10    |
| 1     | 20    |
| 2     | 30    |
| 3     | 40    |
| 4     | 50    |
| 5     | 60    |

-->Accessing Range of Elements:
1. Basic Slicing:
Example:
print(numbers[1:4])
Output:
[20, 30, 40]

Explanation:
* Starts from index `1`
* Stops before index `4`

2. From Beginning:
Example:
print(numbers[:3])
Output:
[10, 20, 30]

3. Till End:
Example:
print(numbers[2:])
Output:
[30, 40, 50, 60]

4. Full List Copy:
Example:
print(numbers[:])
Output:
[10, 20, 30, 40, 50, 60]

- Slicing with Step:
5. Skip Elements:
Example:
print(numbers[0:6:2])
Output:
[10, 30, 50]

Explanation:
- Starts at `0`
- Jumps by `2`

-->Negative Index Slicing:
Example:
print(numbers[-4:-1])
Output:
[30, 40, 50]

-->Reverse a List:
Example:
print(numbers[::-1])
Output:
[60, 50, 40, 30, 20, 10]

=====================================================================================================================================================
-->List Operations:

1. Common list operations: concatenation, repetition, membership.
-->Common List Operations in Python: Python provides many operations that can be performed on lists.
1. Concatenation (+):Concatenation is used to join two lists.
Example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)

2. Repetition (*):Repetition is used to repeat list elements multiple times.
Example:
numbers = [10, 20]
print(numbers * 3)

3. Membership Operators (in and not in):Membership operators check whether an element exists in a list.
Example:
a = [1, 2]
b = [3, 4]
print("Concatenation :", a + b)
print("Repetition    :", a * 2)
print("2 in a        :", 2 in a)
print("5 not in b    :", 5 not in b)

--------------------------------------------------------------------------------------------------------------------------------------------------

2. Understanding list methods like append(), insert(), remove(), pop().
-->append():
- `append()` method is used to add a new element at the end of the list.
- It increases the size of the list by one element.
- The new value is always added at the last position.

-->insert():
- `insert()` method is used to add an element at a specific index position.
- It allows you to place the value anywhere inside the list.
- Existing elements shift to the right after insertion.

-->remove():
- `remove()` method is used to delete a specific value from the list.
- It removes only the first matching element.
- If the value is not found, an error occurs.

-->pop():
- `pop()` method is used to remove an element using its index number.
- If no index is given, it removes the last element of the list.
- It also returns the removed value.

Example:
fruits = ["Apple", "Banana"]
fruits.append("Mango")
fruits.insert(1, "Orange")
fruits.remove("Banana")
fruits.pop()
print(fruits)

-----------------------------------------------------------------------------------------------------------------------------------------------------

-->Working with Lists:

1. Iterating over a list using loops.
-->Iterating Over a List Using Loops:
- Iterating means visiting or accessing each element of a list one by one.
- In Python, loops are used to iterate through list elements easily.
- The two most common loops used for iteration are for loop and while loop.
- A for loop directly accesses elements from the list, while a while loop accesses elements using index numbers.
- Iteration is useful when we want to print, calculate, search, or modify multiple list elements automatically.
- It reduces code repetition and makes programs shorter and easier to understand.

Example:
numbers = [10, 20, 30, 40]
# Using for loop
print("Using for loop")
for i in numbers:
    print(i)
# Using while loop
print("Using while loop")
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
Output:
Using for loop
10
20
30
40
Using while loop
10
20
30
40

---------------------------------------------------------------------------------------------------------------------------------------------------
2. Sorting and reversing a list using sort(), sorted(), and reverse().
-->Sorting and Reversing a List:
- Sorting means arranging list elements in ascending or descending order.
- Reversing means changing the order of elements from last to first.
- Python provides `sort()`, `sorted()`, and `reverse()` methods for these operations.
- These methods help organize data in a proper sequence and make data easier to read and manage.

-->sort():
- `sort()` method is used to sort the original list directly.
- By default, it sorts elements in ascending order.
- It changes the actual list permanently.

-->sorted():
- `sorted()` function is used to sort elements and create a new sorted list.
- It does not change the original list.
- It can be used with lists, tuples, and other iterable objects.

-->reverse():
- `reverse()` method is used to reverse the order of list elements.
- The first element becomes last and the last becomes first.
- It changes the original list directly.

Example:
numbers = [40, 10, 30, 20]
# sort()
numbers.sort()
print("Using sort() :", numbers)
# sorted()
data = [5, 2, 8, 1]
new_list = sorted(data)
print("Using sorted() :", new_list)
# reverse()
data.reverse()
print("Using reverse() :", data)
Output:
Using sort() : [10, 20, 30, 40]
Using sorted() : [1, 2, 5, 8]
Using reverse() : [1, 8, 2, 5]

---------------------------------------------------------------------------------------------------------------------------------------------------

3. Basic list manipulations: addition, deletion, updating, and slicing.
-->Basic List Manipulations in Python:
- List manipulation means performing different operations on list elements such as adding, deleting, updating, and accessing data.
- Python lists are mutable, which means their values can be changed easily after creation.
- These operations help manage and organize data inside a list efficiently.
- Common list manipulations include addition of elements, deletion of elements, updating values, and slicing lists.

-->Addition in List:
- Addition is used to add new elements into a list.
- Elements can be added using methods like append() and insert().
- New values can be added at the end or at a specific position.

-->Deletion in List:
- Deletion is used to remove elements from a list.
- Methods like remove(), pop(), and del are commonly used.
- Elements can be deleted using value or index position.

-->Updating in List:
- Updating means changing an existing element in the list.
- List elements are updated using index numbers.
- The old value is replaced with a new value.

-->Slicing in List:
- Slicing is used to access a range of elements from a list.
- It uses starting and ending index positions.
- Slicing helps retrieve multiple elements at once.

Example:
numbers = [10, 20, 30, 40]
# Addition
numbers.append(50)
# Deletion
numbers.remove(20)
# Updating
numbers[1] = 35
# Slicing
print("Sliced List :", numbers[1:4])
print("Updated List :", numbers)

Output:
Sliced List : [35, 40, 50]
Updated List : [10, 35, 40, 50]

----------------------------------------------------------------------------------------------------------------------------------------------------

-->Tuple:

1. Introduction to tuples, immutability.
-->Introduction to Tuples in Python:
- A tuple is a collection data type used to store multiple elements in a single variable.
- Tuples are written using round brackets ().
- They can store different types of data such as integers, strings, and float values.
- Tuples are ordered and allow duplicate values like lists.

* Immutability of Tuple:
- Tuples are immutable, which means their elements cannot be changed after creation.
- We cannot add, remove, or update elements directly in a tuple.
- This makes tuples more secure and faster compared to lists.
- If modification is needed, a new tuple must be created.

Example:
student = (101, "Riya", 85.5)
print(student)
print(student[1])
Output:
(101, 'Riya', 85.5)
Riya

Example of Immutability:
data = (10, 20, 30)
data[1] = 50
Output:
TypeError: 'tuple' object does not support item assignment

---------------------------------------------------------------------------------------------------------------------------------------------------

2. Creating and accessing elements in a tuple.
-->Creating and Accessing Elements in a Tuple:
- A tuple is a built-in collection data type in Python used to store multiple values in a single variable.
- Tuples are created using round brackets () and elements are separated by commas.
- A tuple can contain different types of data such as integers, strings, float values, and boolean values.
- Tuple elements are ordered, which means the position of each element is fixed and maintained.
- Tuples allow duplicate values and support both positive and negative indexing.
- Elements inside a tuple are accessed using index numbers inside square brackets [].
- Positive indexing starts from 0, while negative indexing starts from -1 from the end.
- Tuples are immutable, meaning their elements cannot be modified, added, or removed after creation.
- Because of immutability, tuples are faster and more secure compared to lists in some situations.

Example:
student = (101, "Riya", "Python", 85.5)
print("Tuple :", student)
print("First Element :", student[0])
print("Second Element :", student[1])
print("Last Element :", student[-1])
Output:
Tuple : (101, 'Riya', 'Python', 85.5)
First Element : 101
Second Element : Riya
Last Element : 85.5

----------------------------------------------------------------------------------------------------------------------------------------------------

3. Basic operations with tuples: concatenation, repetition, membership.
-->Basic Operations with Tuples:
- Tuples support different operations similar to lists.
- Common tuple operations include concatenation, repetition, and membership checking.
- These operations help combine tuples, repeat elements, and check the presence of values.
- Since tuples are immutable, these operations do not modify the original tuple directly.

-->Concatenation in Tuple:
- Concatenation is used to join two or more tuples into a single tuple.
- The + operator is used for concatenation.
- It creates a new tuple containing elements from both tuples.

-->Repetition in Tuple:
- Repetition is used to repeat tuple elements multiple times.
- The * operator is used for repetition.
- It creates a new tuple with repeated elements.

-->Membership in Tuple:
- Membership operators are used to check whether an element exists in a tuple or not.
- in returns True if the element is present.
- not in returns True if the element is absent.

Example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
# Concatenation
print("Concatenation :", tuple1 + tuple2)
# Repetition
print("Repetition :", tuple1 * 2)
# Membership
print("2 in tuple1 :", 2 in tuple1)
print("7 not in tuple1 :", 7 not in tuple1)
Output:
Concatenation : (1, 2, 3, 4, 5)
Repetition : (1, 2, 3, 1, 2, 3)
2 in tuple1 : True
7 not in tuple1 : True

=====================================================================================================================================================

-->Accessing Tuples:

1. Accessing tuple elements using positive and negative indexing.
-->Accessing Tuple Elements Using Positive and Negative Indexing:
- Tuple elements are accessed using index numbers inside square brackets [].
- Python supports both positive indexing and negative indexing in tuples.
- Positive indexing starts from left to right beginning with 0.
- Negative indexing starts from right to left beginning with -1.
- Indexing helps access specific elements from a tuple easily.
- Tuples are ordered, so every element has a fixed index position.

* Positive Indexing:
- In positive indexing, counting starts from the beginning of the tuple.
- The first element has index 0, the second has index 1, and so on.

* Negative Indexing:
- In negative indexing, counting starts from the end of the tuple.
- The last element has index -1, the second last has index -2, and so on.

Example:
fruits = ("Apple", "Banana", "Mango", "Orange")
# Positive Indexing
print("First Element :", fruits[0])
print("Third Element :", fruits[2])
# Negative Indexing
print("Last Element :", fruits[-1])
print("Second Last Element :", fruits[-2])

Output:
First Element : Apple
Third Element : Mango
Last Element : Orange
Second Last Element : Mango

--------------------------------------------------------------------------------------------------------------------------------------------------

2. Slicing a tuple to access ranges of elements.
-->Slicing a Tuple to Access Ranges of Elements:
- Slicing is used to access multiple elements from a tuple at the same time.
- It allows selecting a range of elements using starting and ending index positions.
- Tuple slicing does not change the original tuple because tuples are immutable.
- Slicing can be done using positive indexing as well as negative indexing.
- The ending index is not included in the output.
- It is useful for extracting specific portions of data from a tuple.

syntax:
tuple_name[start : end : step]
- start ? Starting index
- end ? Ending index (not included)
- step ? Increment value (optional)

Example:
numbers = (10, 20, 30, 40, 50, 60)
# Basic slicing
print("numbers[1:4] :", numbers[1:4])
# From beginning
print("numbers[:3] :", numbers[:3])
# Till end
print("numbers[2:] :", numbers[2:])
# Using step
print("numbers[0:6:2] :", numbers[0:6:2])
# Negative indexing slicing
print("numbers[-4:-1] :", numbers[-4:-1])

Output:
numbers[1:4] : (20, 30, 40)
numbers[:3] : (10, 20, 30)
numbers[2:] : (30, 40, 50, 60)
numbers[0:6:2] : (10, 30, 50)
numbers[-4:-1] : (30, 40, 50)

====================================================================================================================================================

-->Dictionaries:

1. Introduction to dictionaries: key-value pairs
-->Introduction to Dictionaries: Key-Value Pairs:
- A dictionary is a built-in data type in Python used to store data in the form of key-value pairs.
- It is created using curly brackets {} and each element contains a key and its corresponding value.
- Keys are used to identify values uniquely inside the dictionary.
- Dictionary elements are separated by commas, and each key is separated from its value using a colon :.
- Dictionaries are mutable, which means values can be added, updated, or removed after creation.
- They are unordered collections and allow storing different types of data together.
- Keys in a dictionary must be unique, but values can be duplicated.
- Dictionaries are useful for storing structured data like student details, employee records, product information, etc.

Example:
student = {
    "id": 101,
    "name": "Riya",
    "course": "Python"
}
print(student)

Output:
{'id': 101, 'name': 'Riya', 'course': 'Python'}

----------------------------------------------------------------------------------------------------------------------------------------------------

2. Accessing, Adding, Updating, and Deleting Dictionary Elements.
-->Accessing, Adding, Updating, and Deleting Dictionary Elements:
- Dictionary elements are stored in the form of key-value pairs.
- Python dictionaries are mutable, so their elements can be accessed, added, updated, and deleted easily.
- Values are accessed using their keys instead of index numbers.
- These operations help manage and organize data efficiently inside a dictionary.

-->Accessing Dictionary Elements:
- Dictionary values are accessed using keys inside square brackets [].
- The key is used to retrieve its corresponding value.
- If the key does not exist, an error occurs.

-->Adding Dictionary Elements:
- New elements can be added by assigning a value to a new key.-
- If the key does not already exist, it gets added to the dictionary.
- The new key-value pair is stored inside the dictionary.

-->Updating Dictionary Elements:
- Dictionary values can be updated using existing keys.
- The old value is replaced with the new value.
- Only the specified key’s value changes.

-->Deleting Dictionary Elements:
- Dictionary elements can be deleted using del, pop(), or clear() methods.
- Deletion removes a key-value pair from the dictionary.
- After deletion, that key no longer exists in the dictionary.

Example:
student = {
    "id": 101,
    "name": "Riya",
    "course": "Python"
}
# Accessing
print("Name :", student["name"])
# Adding
student["city"] = "Ahmedabad"
# Updating
student["course"] = "Python Full Stack"
# Deleting
del student["id"]
print("Updated Dictionary :", student)

Output:
Name : Riya
Updated Dictionary : {'name': 'Riya', 'course': 'Python Full Stack', 'city': 'Ahmedabad'}

--------------------------------------------------------------------------------------------------------------------------------------------------

3.  Dictionary methods like keys(), values(), and items().
-->Dictionary Methods: keys(), values(), and items():
- Python dictionaries provide different built-in methods to access and work with dictionary data easily.
- Methods like keys(), values(), and items() are commonly used to retrieve dictionary information.
- These methods help access only keys, only values, or both keys and values together.
- They are very useful while iterating and managing dictionary data.

-->keys() Method:
- The keys() method is used to get all the keys from a dictionary.
- It returns a view object containing only dictionary keys.
- This method is useful when we want to access or iterate through keys only.

-->values() Method:
- The values() method is used to get all the values from a dictionary.
- It returns a view object containing only dictionary values.
- This method helps access all stored values easily.

-->items() Method:
- The items() method is used to get both keys and values together.
- It returns key-value pairs in the form of tuples.
- This method is commonly used while looping through dictionaries.

Example:
student = {
    "id": 101,
    "name": "Riya",
    "course": "Python"
}
# keys()
print("Keys :", student.keys())
# values()
print("Values :", student.values())
# items()
print("Items :", student.items())

Output:
Keys : dict_keys(['id', 'name', 'course'])
Values : dict_values([101, 'Riya', 'Python'])
Items : dict_items([('id', 101), ('name', 'Riya'), ('course', 'Python')])

====================================================================================================================================================

--> Working with Dictionaries

1. Iterating over a dictionary using loops.
-->Iterating Over a Dictionary Using Loops:
- Iterating over a dictionary means accessing its keys, values, or key-value pairs one by one using loops.
- Python mainly uses the for loop for dictionary iteration.
- Dictionaries can be iterated using methods like keys(), values(), and items().
- Iteration helps perform operations on dictionary data easily and efficiently.
- It is useful for displaying, searching, updating, and processing dictionary elements.

-->Iterating Through Keys:
- By default, a for loop accesses dictionary keys one by one.
- The loop variable stores each key during iteration.

-->Iterating Through Values:
- The values() method is used to access only dictionary values.
- It returns all values stored inside the dictionary.

-->Iterating Through Key-Value Pairs:
- The items() method is used to access both keys and values together.
- It returns elements in tuple form (key, value).

Example:
student = {
    "id": 101,
    "name": "Riya",
    "course": "Python"
}
# Iterating through keys
print("Keys")
for k in student:
    print(k)
# Iterating through values
print("Values")
for v in student.values():
    print(v)
# Iterating through key-value pairs
print("Key-Value Pairs")
for k, v in student.items():
    print(k, ":", v)
	
Output:
Keys
id
name
course

Values
101
Riya
Python

Key-Value Pairs
id : 101
name : Riya
course : Python

-------------------------------------------------------------------------------------------------------------------------------------------------

2. Merging two lists into a dictionary using loops or zip().
-->Merging Two Lists into a Dictionary Using Loops or zip():
- Two separate lists can be combined to create a dictionary in Python.
- One list is usually used for dictionary keys and the other list for dictionary values.
- This process is called merging lists into a dictionary.
- Python provides different ways to perform this task, such as using loops and the zip() function.
- It is useful for organizing related data into key-value pairs efficiently.

-->Using Loops:
- A loop can be used to access elements from both lists one by one.
- The elements are then stored inside a dictionary as key-value pairs.
- This method gives more control over the merging process.

-->Using zip() Function:
- The zip() function combines elements of two lists together.
- It pairs corresponding elements from both lists.
- The dict() function can then convert these pairs into a dictionary directly.

Example:
keys = ["id", "name", "course"]
values = [101, "Riya", "Python"]
# Using loop
data1 = {}
for i in range(len(keys)):
    data1[keys[i]] = values[i]

print("Using Loop :", data1)
# Using zip()
data2 = dict(zip(keys, values))
print("Using zip() :", data2)

Output:
Using Loop : {'id': 101, 'name': 'Riya', 'course': 'Python'}
Using zip() : {'id': 101, 'name': 'Riya', 'course': 'Python'}

---------------------------------------------------------------------------------------------------------------------------------------------------

3. Counting occurrences of characters in a string using dictionaries.
-->Counting Occurrences of Characters in a String Using Dictionaries:
- A dictionary can be used to count how many times each character appears in a string.
- In this method, characters are stored as dictionary keys and their counts are stored as values.
- When a character appears again, its count is increased by 1.
- This technique is useful for frequency counting, text analysis, and data processing tasks.
- Loops and conditional statements are commonly used to perform this operation.

Example:
text = "python"
count = {}
for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
print(count)

Output:
{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

Example with Repeated Characters:
text = "banana"
count = {}
for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)

Output:
{'b': 1, 'a': 3, 'n': 2}

====================================================================================================================================================

-->Functions

1. Defining functions in Python
-->Defining Functions in Python:
- A function is a block of reusable code used to perform a specific task.
- Functions help reduce code repetition and make programs shorter, organized, and easier to understand.
- In Python, functions are defined using the def keyword followed by the function name and parentheses ().
- A function can be called whenever needed in the program.
- Functions improve code reusability, readability, and program management.
- They can accept input values called parameters and may also return output values.

Syntax:
def function_name():
    statements
- def ? keyword used to define a function
- function_name ? name of the function
- Function body contains the code to execute

Example:
def greet():
    print("Welcome to Python")
greet()

output:
Welcome to Python

Example with Parameters:
def add(a, b):
    print("Addition :", a + b)
add(10, 20)

output:
Addition : 30

---------------------------------------------------------------------------------------------------------------------------------------------------

2. Different types of functions: with/without parameters, with/without return values.

1. Function Without Parameters and Without Return Value
- This type of function does not take any input from the user.
- It also does not return any value.
- It only performs a task and displays output.
Example:
def greet():
    print("Hello World")
greet()

2. Function With Parameters and Without Return Value
- This function takes input using parameters.
- It performs a task but does not return any value.
Example:
def add(a, b):
    print("Addition =", a + b)
add(10, 20)

3. Function Without Parameters and With Return Value
- This function does not take any input.
- It returns a value using return.
Example:
def get_number():
    return 100
x = get_number()
print(x)

4. Function With Parameters and With Return Value
- This function takes input through parameters.
- It also returns a value after processing.
Example:
def multiply(a, b):
    return a * b
result = multiply(5, 4)
print("Multiplication =", result)

----------------------------------------------------------------------------------------------------------------------------------------------------

3. Anonymous functions (lambda functions).

-->Anonymous Function (Lambda Function):
- An anonymous function is a function that does not have a function name.
- In Python, anonymous functions are created using the lambda keyword.
- Lambda functions are also called single-line functions because they are written in one line.
- They are mainly used for short and simple operations.
- A lambda function can take any number of arguments, but it can contain only one expression.
- The value of the expression is automatically returned.
- Lambda functions are commonly used with functions like map(), filter(), and sorted().
Syntax:
lambda arguments : expression
Example:
add = lambda a, b: a + b
print(add(10, 20))
output:
30

===================================================================================================================================================

																	Modules
																	
1. Introduction to Python modules and importing modules.
-->Introduction to Python Modules:
- A module in Python is a file that contains functions, variables, or classes.
- Modules help us organize code properly and reuse code in different programs.
- Instead of writing the same code again and again, we can create a module and import it whenever needed.
- Python provides two types of modules:
       Built-in Modules
       User-defined Modules
- Examples of built-in modules are math, random, and datetime.

-->Importing Modules:
- To use a module in a Python program, we use the import keyword.
- After importing, we can access the functions and features of that module.
Syntax:
import module_name
Example:
import math
print(math.sqrt(25))
output:
5.0

---------------------------------------------------------------------------------------------------------------------------------------------------

2. Standard library modules: math, random.
-->Standard Library Modules in Python:
- Python provides many built-in modules called standard library modules.
- These modules contain ready-made functions that help perform different tasks easily.
- We can use these modules by importing them into our program.
- math and random are commonly used standard library modules.

1. Math Module:
Description:
The math module is used for mathematical calculations.
It provides functions like square root, power, factorial, trigonometry, etc.
Example:
import math
print(math.sqrt(36))
output:
6.0

2. Random Module:
Description:
- The random module is used to generate random values.
- It helps generate random numbers, random choices, and more.
Example:
import random
print(random.randint(1, 10))
output:
5

-----------------------------------------------------------------------------------------------------------------------------------------------------

3. Creating custom modules.

-->Creating Custom Modules in Python:
- A custom module is a module created by the user.
- It is used to store functions, variables, or classes in a separate Python file.
- Custom modules help in code reusability and better program organization.
- The file must be saved with a .py extension.
- We can use the module in another program by using the import keyword.
Example:
mymodule.py
def add(a, b):
    return a + b
Main Program:
import mymodule
print(mymodule.add(10, 20))
output:
30

=====================================================================================================================================================