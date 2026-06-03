																◆ Introduction to Python Theory ◆ 
								
1. Introduction to Python and its Features (simple, high-level, interpreted language).
-->Introduction:Python is a powerful, easy-to-learn, and widely used programming language. It was developed by Guido van Rossum and released in 1991. Python was designed with the main goal of making programming simple, readable, and efficient.
- Python is called a general-purpose programming language because it can be used for many types of software development such as:
	1)Web development
	2)Desktop applications
	3)Game development
	4)Artificial Intelligence (AI)
	5)Machine Learning
	6)Data Science
	7)Automation
	8)Cybersecurity
	9)Mobile applications

-->Features:
1)Simple:
Python is known for its simple and readable syntax. The language is designed in such a way that programmers can easily understand and write code without much difficulty. Python uses English-like keywords and simple structure, which makes programs look clean and easy to read.
Example :
name = "Riya Jivani"
print("Welcome", name)
2)High-level:
- Python is a high-level programming language. This means programmers do not need to manage hardware details such as memory allocation, processor operations, or system architecture manually.
- Python provides simple commands and built-in functions that make programming easier and faster. It allows developers to focus on solving problems and writing application logic instead of dealing with low-level technical details.
- High-level languages are closer to human language, so they are easier to read, write, and understand compared to low-level languages like Assembly or Machine Language.
3)interpreted language:
- Python is an interpreted language. This means Python code is executed line by line by a program called an interpreter.
- Unlike compiled languages, Python does not require the entire program to be compiled before execution. The interpreter reads the code, translates it into machine language, and executes it immediately. This makes Python easier to test, debug, and develop.
- Because Python executes code line by line:
	Errors can be found quickly
	Program testing becomes easier
	Development speed increases
	Beginners can understand execution flow easily

-----------------------------------------------------------------------------------------------------------------------------------------------------

2. History and evolution of Python.
-->History:Python was created by Guido van Rossum in 1989 at CWI (Netherlands). It was designed as a simple, easy-to-read, and powerful programming language.
- The first version, Python 0.9.0, was released in 1991. Later:
	Python 1.0 was released in 1994
	Python 2.0 was released in 2000
	Python 3.0 was released in 2008 with many improvements
- Python was named after the comedy show Monty Python's Flying Circus.
- Today, Python is widely used in web development, artificial intelligence, data science, automation, and software development because of its simple syntax and powerful features.

-->Evolution:Python has evolved through different versions with improved features and performance.
- Python 1.0 (1994)
	First official version
	Added functions, modules, and exception handling
- Python 2.0 (2000)
	Introduced garbage collection
	Added Unicode support
	Improved memory management
- Python 3.0 (2008)
	Improved syntax and readability
	Better Unicode support
	Removed old features of Python 2
	print became a function
Example:
print("Riya Jivani")

- Today, Python 3 is widely used in:
	Artificial Intelligence
	Data Science
	Web Development
	Automation
	Machine Learning
	
-----------------------------------------------------------------------------------------------------------------------------------------------------
	
3. Advantages of using Python over other programming languages.
-->Advantages:
1)Easy to Learn and Use:
- Python has simple and readable syntax similar to English, making it beginner-friendly.

2)Less Coding Required:
- Python programs are shorter compared to many other programming languages like C++ or Java.

3)High-Level Language:
- Python handles memory management and other complex tasks automatically.

4)Interpreted Language:
- Python executes code line by line, making debugging easier and faster.

5)Cross-Platform Support:
- Python programs can run on:
	Windows
	Linux
	macOS
without changing the code.

6)Large Standard Library:
- Python provides many built-in libraries and modules for:
	Web development
	Data science
	Machine learning
	Automation
	Game development

7)Supports Multiple Programming Paradigms:
- Python supports:
	Object-Oriented Programming
	Functional Programming
	Procedural Programming

8)Open Source and Free:
- Python is free to download and use.

9)Huge Community Support:
- Python has a large developer community that provides tutorials, libraries, and solutions.

10)Widely Used in Modern Technologies:
- Python is used in:
	Artificial Intelligence
	Machine Learning
	Data Science
	Cybersecurity
	Web Development
- Many companies use Python, including:
	Google
	Netflix
	Instagram
	
-----------------------------------------------------------------------------------------------------------------------------------------------------

4. Installing Python and setting up the development environment (Anaconda, PyCharm, or VS Code).
-->vs code:
Step 1: Install Python
1)Go to: Python.org Downloads
2)Download Python
3)Run setup
4)Tick “Add Python to PATH”
5)Click Install Now

Step 2: Verify Python Installation
- Open Command Prompt (CMD) and type:
	python --version
- If Python is installed correctly, it will display the Python version.
Example:
	Python 3.13.0
	
Step 3: Download and Install VS Code
1)Open official VS Code website
2)Download VS Code for your operating system.
3)Run the installer and complete installation.

Step 4: Install Python Extension
1)Open VS Code
2)Go to Extensions
3)Search Python
4)Install Python extension by Microsoft

Step 5: Run Python Program
->Create file:
	hello.py
->Write code:
	print("Hello World")
->Run in terminal:
	python hello.py
->Output:
	Hello World
	
-----------------------------------------------------------------------------------------------------------------------------------------------------

5. Writing and executing your first Python program.
Step 1: Open Visual Studio Code
Open VS Code after installing Python.

Step 2: Create Python File
Create a new file with .py extension.
Example:
	hello.py
	
Step 3: Write Python Program
Type the following code:
print("Hello World")

Step 4: Save the File
Press:
Ctrl + S

Step 5: Run the Program
Open terminal and type:
python hello.py

Output:
Hello World

=====================================================================================================================================================

															◆ Programming Style ◆ 

1. Understanding Python’s PEP 8 guidelines.
-->Understanding PEP 8 Guidelines:
	- PEP 8 stands for Python Enhancement Proposal 8. It is the official style guide for writing clean and readable Python code.
	- PEP 8 helps programmers write code in a proper and consistent format so that it becomes easier to read, understand, and maintain.

-->Main PEP 8 Guidelines:
1. Use Proper Indentation
Use 4 spaces for indentation.
Example:
	if True:
		print("Hello")
		
2. Variable Names
Use lowercase letters and underscores.
Example:
	student_name = "Riyu"
	
3. Class Names
Use CapitalizedWords format.
Example:
	class StudentData:
		pass
		
4. Add Spaces Around Operators
Example:
a = 10
b = 20
total = a + b

5. Keep Line Length Short
Maximum recommended line length is 79 characters.

6. Use Blank Lines Properly
Use blank lines between functions and classes to improve readability.

-----------------------------------------------------------------------------------------------------------------------------------------------------

2. Indentation, comments, and naming conventions in Python.
-->Indentation:
- Indentation means adding spaces at the beginning of a line to define a block of code.
- Python uses indentation instead of brackets.
- Usually, 4 spaces are used for indentation.
Example:
	if 5 > 2:
		print("Five is greater")
- Importance of Indentation
- Makes code readable
- Defines code blocks
- Prevents syntax errors

-->Comments:
- Comments are used to explain the code.
- Python ignores comments during execution.
- Comments start with #.
Example:
**This is single line comment**
	print("Hello")

**This is multi line comment**
	"""
	This is
	a multi-line comment
	"""
- Importance of Comments
- Makes code understandable
- Helps during debugging
- Improves documentation

-->Naming Conventions:
- Naming conventions are rules for giving names to variables, functions, classes, etc.

1) Variable Names
- Use lowercase letters and underscores.
Example:
	student_name = "Riyu"

2)Function Names
- Function names should also use lowercase and underscores.
Example:
	def calculate_sum():
		pass
		
3)Class Names
- Use CapitalizedWords format.
Example:
	class StudentData:
		pass
		
4)Constant Names
- Constants are written in uppercase letters.
Example:
	PI = 3.14
	
- Importance of Naming Conventions
- Improves readability
- Makes code clean and professional
- Easier maintenance
- Better teamwork

-----------------------------------------------------------------------------------------------------------------------------------------------------

3. Writing readable and maintainable code.
-->Readable and maintainable code means writing programs that are easy to understand, modify, and debug. Clean code helps both the programmer and other developers work efficiently.

*Tips for Writing Readable and Maintainable Code:
1)Use Meaningful Variable Names:
- Use clear and understandable names.
Good Example:
	student_name = "Riyu"
Bad Example:
	sn = "Riyu"
2)Follow Proper Indentation:
- Use 4 spaces for indentation.
Example:
	if True:
		print("Hello")
3)Write Comments:
- Comments explain the purpose of the code.
Example:
	#Calculate total marks
	total = 90 + 85
4)Keep Code Simple:
- Avoid unnecessary complexity.
Example:
	a = 10
	b = 20
	print(a + b)
5)Use Functions:
- Functions make code reusable and organized.
Example:
	def greet():
		print("Welcome")
	greet()
6)Follow PEP 8 Guidelines:
- PEP 8 provides coding standards for clean Python code.
7)Avoid Long Lines:
- Keep lines short and readable.

=====================================================================================================================================================

																◆ Core Python Concepts ◆ 
											
1. Understanding data types: integers, floats, strings, lists, tuples, dictionaries, sets.
-->Integer(int):
	Integers are whole numbers without decimal points.
Example:
	age = 20
	print(age)
Output:
	20
-->Float(float):
	Floats are numbers with decimal points.
Example:
	price = 10.5
	print(price)
Output:
	10.5
-->String(str):
	Strings store text or characters inside quotes.
Example:
	name = "Riyu"
	print(name)
Output:
	Riyu
-->List(list):
	Lists store multiple values and can be changed (mutable).
Example:
	numbers = [10, 20, 30]
	print(numbers)
Output:
	[10, 20, 30]
-->Tuple(tuple):
	Tuples store multiple values but cannot be changed (immutable).
Example:
	colors = ("red", "blue", "green")
	print(colors)
Output:
	('red', 'blue', 'green')
-->Dictionary(dict):
	Dictionaries store data in key-value pairs.
Example:
	student = {
		"name": "Riyu",
		"age": 20
	}
	print(student)
Output:
	{'name': 'Riyu', 'age': 20}
-->Set(set):
	Sets store unique values and do not allow duplicates.
Example:
	nums = {1, 2, 3, 3}
	print(nums)
Output:
	{1, 2, 3}
	
-----------------------------------------------------------------------------------------------------------------------------------------------------
	
2. Python variables and memory allocation.
-->Python Variables:
- A variable is a name used to store data in memory.
- Variables help programmers store and use values in a program.
Example:
	name = "Riyu"
	age = 20
**Rules for Variable Names
	1)Variable names can contain letters, numbers, and underscores
	2)Variable names cannot start with a number
	3)Spaces are not allowed
	4)Python keywords cannot be used
Example:
	student_name = "Riyu"
	age1 = 20

-->Memory Allocation:
- Memory allocation means storing data in computer memory.
- In Python, memory is automatically managed by the Python interpreter. When a variable is created, Python automatically allocates memory for that value.
Example:
	x = 10
*Dynamic Typing:
- Python is dynamically typed, so there is no need to declare data types manually.
Example:
	x = 10
	x = "Hello"
- The same variable can store different data types.
*Multiple Variable Assignment:
Example:
	a, b, c = 10,20,30
	print(a, b, c)
Output:
	10 20 30
	
---------------------------------------------------------------------------------------------------------------------------------------------------
	
3. Python operators: arithmetic, comparison, logical, bitwise.
1)Arithmetic Operators:
| Operator | Name           | Example   | Output |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `10 + 5`  | `15`   |
| `-`      | Subtraction    | `10 - 5`  | `5`    |
| `*`      | Multiplication | `10 * 5`  | `50`   |
| `/`      | Division       | `10 / 5`  | `2.0`  |
| `%`      | Modulus        | `10 % 3`  | `1`    |
| `**`     | Exponent       | `2 ** 3`  | `8`    |
| `//`     | Floor Division | `10 // 3` | `3`    |

2)Comparison Operators:
| Operator | Meaning               | Example    | Output  |
| -------- | --------------------- | ---------- | ------- |
| `==`     | Equal to              | `10 == 10` | `True`  |
| `!=`     | Not Equal to          | `10 != 5`  | `True`  |
| `>`      | Greater Than          | `10 > 5`   | `True`  |
| `<`      | Less Than             | `10 < 5`   | `False` |
| `>=`     | Greater Than Equal To | `10 >= 10` | `True`  |
| `<=`     | Less Than Equal To    | `10 <= 5`  | `False` |

3)Logical Operators:
| Operator | Meaning                | Example        | Output  |
| -------- | ---------------------- | -------------- | ------- |
| `and`    | Both conditions true   | `5>2 and 10>5` | `True`  |
| `or`     | Any one condition true | `5>10 or 10>5` | `True`  |
| `not`    | Reverse condition      | `not(5>2)`     | `False` |

4)Bitwise Operators:
| Operator | Meaning     | Example  | Output |
| -------- | ----------- | -------- | ------ |
| `&`      | AND         | `5 & 3`  | `1`    |
| `\|`     | OR          | `5 \| 3` | `7`    |
| `^`      | XOR         | `5 ^ 3`  | `6`    |
| `~`      | NOT         | `~5`     | `-6`   |
| `<<`     | Left Shift  | `5 << 1` | `10`   |
| `>>`     | Right Shift | `5 >> 1` | `2`    |

***LAB***
• Practical Example 1: How does the Python code structure work?
-->Python Code Structure:
- In Python, the code structure is simple and easy to understand. Python programs are written line by line, and the interpreter executes them in the same order.
- Python uses indentation (spaces) to define blocks of code instead of curly brackets {} used in many other languages.
*A Python program generally contains:
	Variables
	Statements
	Conditions
	Functions
	Comments
	Proper indentation
Example:
	#Simple Python Program
	name = "Riyu"
	if name == "Riyu":
		print("Welcome", name)
Explanation:
# Simple Python Program is a comment.
• name = "Riyu" stores data in a variable.
• if checks the condition.
• Indented print() statement belongs to the if block.
Output:
	Welcome Riyu
	
• Practical Example 2: How to create variables in Python?
-->Creating Variables in Python:
- Variables are used to store data values in memory.
- In Python, variables are created automatically when a value is assigned to them. There is no need to declare the data type manually.
*Rules for Variables:
	1)Variable names can contain letters, numbers, and underscores.
	2)Variable names cannot start with numbers.
	3)Spaces are not allowed.
	4)Python keywords cannot be used as variable names.
Example:
	name = "Riyu"
	age = 20
	price = 99.5
	print(name)
	print(age)
	print(price)
Explanation:
• name stores a string value.
• age stores an integer value.
• price stores a float value.
Output:
	Riyu
	20
	99.5
- Advantages of Variables
	Easy data storage
	Reusable values
	Improves program flexibility

• Practical Example 3: How to take user input using the input() function.
-->Taking User Input Using input():
- The input() function is used to take data from the user during program execution.
- By default, input data is stored as a string.
Example:
	name = input("Enter your name: ")
	print("Hello", name)
Explanation:
• input() displays a message to the user.
• The entered value is stored in the variable name.
• print() displays the output.
Output:
	Enter your name: Riyu
	Hello Riyu
*Taking Integer Input:
	age = int(input("Enter age: "))
	print(age)
- Advantages of input()
	Makes programs interactive
	Allows dynamic data entry
	Useful for real-world applications
	
• Practical Example 4: How to check the type of a variable dynamically using type().
-->Checking Variable Type Using type():
- Python is a dynamically typed language, meaning variables can store different types of data automatically.
- The type() function is used to check the data type of a variable.
Example:
	a = 10
	b = 99.5
	c = "Python"
	d = True
	print(type(a))
	print(type(b))
	print(type(c))
	print(type(d))
Explanation:
• a is an integer
• b is a float
• c is a string
• d is a boolean
- type() identifies the data type stored in each variable.
Output:
	<class 'int'>
	<class 'float'>
	<class 'str'>
	<class 'bool'>
- Importance of type()
	Helps in debugging
	Useful for checking data types
	Improves program accuracy
	
=====================================================================================================================================================

														◆ Conditional Statements ◆ 
									
1. Introduction to conditionalstatements: if, else, elif.
-->Conditional statements are used to make decisions in a program. They allow the program to execute different blocks of code based on certain conditions.
*Python provides:
	if
	else
	elif
for decision-making.

1)if Statement:
- The if statement executes a block of code only if the condition is True.
Syntax:
	if condition:
		statement
Example:
	age = 18
	if age >= 18:
		print("Eligible for voting")
Output:
	Eligible for voting
Explanation:
• The condition age >= 18 is checked.
• Since the condition is true, the statement is executed.

2)else Statement:
- The else statement executes when the condition is False.
Syntax:
	if condition:
		statement
	else:
		statement
Example:
	age = 15
	if age >= 18:
		print("Eligible for voting")
	else:
		print("Not eligible for voting")
Output:
	Not eligible for voting
Explanation:
• The condition is false.
• Therefore, the else block is executed.

3)elif Statement:
- The elif statement means “else if”.
- It is used to check multiple conditions.
Syntax:
	if condition:
		statement
	elif condition:
		statement
	else:
		statement
Example:
	marks = 75
	if marks >= 90:
		print("Grade A")
	elif marks >= 60:
		print("Grade B")
	else:
		print("Fail")
Output:
	Grade B
Explanation:
• First condition is false.
• Second condition is true.
• Therefore, "Grade B" is printed.

----------------------------------------------------------------------------------------------------------------------------------------------------

2. Nested if-else conditions.
-->A nested if-else condition means placing one if-else statement inside another if-else statement.
- Nested conditions are used when multiple conditions need to be checked step by step.
Syntax:
	if condition1:
		if condition2:
			statement
		else:
			statement
	else:
		statement
Example: Largest Number
	a = 10
	b = 20
	c = 15
	if a > b:
		if a > c:
			print("A is largest")
		else:
			print("C is largest")
	else:
		if b > c:
			print("B is largest")
		else:
			print("C is largest")
Output:
	B is largest
	
=====================================================================================================================================================
	
															◆ Looping (For, While) ◆
											
1. Introduction to for and while loops.
-->Loops are used to execute a block of code repeatedly until a condition is satisfied.
- Python mainly provides:
	for loop
	while loop
	
1)for Loop:
- The for loop is used to iterate over a sequence such as:
	List
	Tuple
	String
	Range
- It is mainly used when the number of repetitions is known.
Syntax:
	for variable in sequence:
		statement
Example:
	for i in range(1, 6):
		print(i)
Output:
	1
	2
	3
	4
	5
Explanation:
• range(1, 6) generates numbers from 1 to 5
• Loop runs repeatedly
• Each value is stored in variable i
• print(i) displays the values

2)while Loop:
- The while loop executes as long as the condition is True.
- It is mainly used when the number of repetitions is not fixed.
Syntax:
	while condition:
		statement
Example:
	i = 1
	while i <= 5:
		print(i)
		i += 1
Output:
	1
	2
	3
	4
	5
Explanation:
• i = 1 initializes the variable
• Condition i <= 5 is checked
• Loop executes while condition is true
•i += 1 increases the value of i

-----------------------------------------------------------------------------------------------------------------------------------------------------

2. How loops work in Python.
-->In Python,loops are used to repeat a block of code multiple times.
Python mainly has 2 types of loops:
	1. for loop
	2. while loop
1)for Loop:
- A `for` loop is used when you know how many times you want to repeat something.
Syntax"
	for variable in sequence:
			statement
Example: Print numbers
	for i in range(5):
		print(i)
Output:
	0
	1
	2
	3
	4
Explanation:
• `range(5)` gives numbers from `0` to `4`
• Loop runs 5 times
• Each time `i` gets a new value

Example: Print names
	names = ["Riya", "Gautamee", "Kruti"]
	for name in names:
		print(name)
Output:
	Riya
	Gautamee
	Kruti
Explanation:
• Loop goes through each item in the list one by one.

2)while Loop:
- A `while` loop runs until a condition becomes False.
Syntax:
	while condition:
		 code

Example: Print numbers
	i = 1
	while i <= 5:
		print(i)
		i = i + 1
Output:
	1
	2
	3
	4
	5
Explanation:
• Start with `i = 1`
• Loop runs while `i <= 5`
• `i = i + 1` increases value each time
- Without increasing `i`, loop becomes infinite.

-> Infinite Loop Example:
	i = 1
	while i <= 5:
		print(i)
- This runs forever because `i` never changes.

-> break Statement:
- `break` stops the loop immediately.
Example:
	for i in range(10):
		if i == 5:
			break
		print(i)
Output:
	0
	1
	2
	3
	4

->continue Statement:
- `continue` skips the current iteration.
Example:
	for i in range(5):
		if i == 2:
			continue
		print(i)
Output:
	0
	1
	3
	4

# Difference Between for and while

| for loop                                 | while loop                                     |
| ---------------------------------------- | ---------------------------------------------- |
| Used when number of repetitions is known | Used when condition-based repetition is needed |
| Easier for lists and ranges              | Better for unknown repetitions                 |

3)Nested Loop:
- Loop inside another loop.
Example:
	for i in range(3):
		for j in range(2):
			print(i, j)
Output:
	0 0
	0 1
	1 0
	1 1
	2 0
	2 1

----------------------------------------------------------------------------------------------------------------------------------------------------

3. Using loops with collections (lists, tuples, etc.).
-->In Python, loops are commonly used with *collections* like:
	* Lists
	* Tuples
	* Strings
	* Dictionaries
	* Sets
- A loop helps access each item one by one.

1)Loop with List:
- A list stores multiple values.
Example:
	fruits = ["Apple", "Banana", "Mango"]
	for fruit in fruits:
		print(fruit)
Output:
	Apple
	Banana
	Mango
Explanation:
• Loop takes each item from the list
• Stores it in `fruit`
• Prints it

2)Loop with Tuple:
- Tuple works similar to list but values cannot change.
Example:
	numbers = (10, 20, 30)
	for num in numbers:
		print(num)
Output:
	10
	20
	30
	
3)Loop with String:
- String is a collection of characters.
Example:
	name = "Python"
	for ch in name:
		print(ch)
Output:
	P
	y
	t
	h
	o
	n

4)Loop with Dictionary:
- Dictionary stores data in `key : value` form.
Example 1: Print Keys
	student = {
		"name": "Rahul",
		"age": 20,
		"city": "Rajkot"
	}
	for key in student:
		print(key)
Output:
	name
	age
	city
Example 2: Print Values
	for value in student.values():
		print(value)
Output:
	Rahul
	20
	Rajkot
Example 3: Print Key and Value
	for key, value in student.items():
		print(key, ":", value)
Output:
	name : Rahul
	age : 20
	city : Rajkot

5)Loop with Set:
- Set stores unique values.
Example:
	colors = {"Red", "Blue", "Green"}
	for color in colors:
		print(color)
Output:
	Blue
	Green
	Red
	
->Using range() with Loops:
- `range()` generates numbers.
Example:
	for i in range(1, 6):
		print(i)
Output:
	1
	2
	3
	4
	5

->Access List Using Index:
Example:
	fruits = ["Apple", "Banana", "Mango"]
	for i in range(len(fruits)):
		print(i, fruits[i])
Output:
	0 Apple
	1 Banana
	2 Mango

->Nested Loop with List:
Example:
	matrix = [
		[1, 2],
		[3, 4]
	]
	for row in matrix:
		for value in row:
			print(value)
Output:
	1
	2
	3
	4

->Common Operations Using Loops:
*Sum of List:
	numbers = [10, 20, 30]
	total = 0
	for num in numbers:
		total = total + num
	print(total)
Output:
	60

*Find Even Numbers:
	numbers = [1, 2, 3, 4, 5, 6]
	for num in numbers:
		if num % 2 == 0:
			print(num)
Output:
	2
	4
	6


====================================================================================================================================================

										◆ Control Statements (Break, Continue, Pass) ◆
									
1. Understanding the role of break, continue, and pass in Python loops.
-->
| Keyword    | Purpose                                   |
| ---------- | ----------------------------------------- |
| `break`    | Stops the loop completely                 |
| `continue` | Skips current iteration and moves to next |
| `pass`     | Does nothing (placeholder statement)      |

1) break Statement:
- Used to exit the loop immediately.
Example:
	for i in range(1, 6):
		if i == 3:
			break
		print(i)
Output:
	1
	2

2) continue Statement:
- Used to skip the current iteration.
Example:
	for i in range(1, 6):
		if i == 3:
			continue
		print(i)
Output:
	1
	2
	4
	5
	
3) pass Statement:
- Used as an empty placeholder.
Example:
	for i in range(5):
		if i == 3:
			pass
		print(i)
Output:
	0
	1
	2
	3
	4
	
Difference:
| `break`                | `continue`               | `pass`                |
| ---------------------- | ------------------------ | --------------------- |
| Stops loop             | Skips iteration          | Does nothing          |
| Exits loop completely  | Moves to next iteration  | Placeholder statement |
| Used to terminate loop | Used to ignore condition | Used for empty blocks |

===================================================================================================================================================

															◆ String Manipulation ◆
															
1. Understanding how to access and manipulate strings.
-->Accessing and Manipulating Strings in Python:
- A string is a sequence of characters written inside quotes.
Example:
	text = "Python"
->Accessing Strings:
* Using Index:
- Each character has a position called an index.
Example:
	text = "Python"
	print(text[0])
	print(text[1])
Output:
	p
	y
*Negative Index:
Example:
	text = "Python"
	print(text[-1])
Output:
	n

->string slicing:
- Used to get part of a string.
Example:
	text = "Python"
	print(text[0:3])
	print(text[2:6])
Output:
	Pyt
	thon
	
**String Manipulation**
| Method         | Description                                               |
| -------------- | --------------------------------------------------------- |
| `upper()`      | Converts string to uppercase                              |
| `lower()`      | Converts string to lowercase                              |
| `title()`      | Converts first letter of each word to uppercase           |
| `capitalize()` | Converts first character to uppercase                     |
| `swapcase()`   | Changes uppercase to lowercase and lowercase to uppercase |
| `strip()`      | Removes spaces from both sides                            |
| `lstrip()`     | Removes spaces from left side                             |
| `rstrip()`     | Removes spaces from right side                            |
| `replace()`    | Replaces old text with new text                           |
| `split()`      | Splits string into list                                   |
| `join()`       | Joins elements into one string                            |
| `find()`       | Finds position of substring                               |
| `index()`      | Returns index of substring                                |
| `count()`      | Counts occurrences of substring                           |
| `startswith()` | Checks if string starts with given text                   |
| `endswith()`   | Checks if string ends with given text                     |
| `isalpha()`    | Checks whether all characters are alphabets               |
| `isdigit()`    | Checks whether all characters are digits                  |
| `isalnum()`    | Checks whether string contains alphabets and numbers      |
| `islower()`    | Checks whether string is lowercase                        |
| `isupper()`    | Checks whether string is uppercase                        |
| `isspace()`    | Checks whether string contains only spaces                |
| `center()`     | Aligns string at center                                   |
| `ljust()`      | Aligns string to left                                     |
| `rjust()`      | Aligns string to right                                    |
| `zfill()`      | Adds zeros at beginning                                   |
| `partition()`  | Splits string into three parts                            |
| `splitlines()` | Splits string by lines                                    |
| `encode()`     | Converts string into encoded bytes                        |
| `casefold()`   | Converts string to lowercase strongly                     |
| `format()`     | Formats string with values                                |


Example:
	text1 = "python"
	text2 = "PYTHON"
	text3 = "hello world"
	text4 = "PyThOn"
	text5 = " hi "
	text6 = "I like Java"
	text7 = "a b c"
	text8 = "python"
	text9 = "apple"
	text10 = "Python"
	text11 = "123"
	text12 = "abc123"
	text13 = "   "
	text14 = "hello-world"
	text15 = "a\nb"
	text16 = "hello"
	print("upper():", text1.upper())
	print("lower():", text2.lower())
	print("title():", text3.title())
	print("capitalize():", text1.capitalize())
	print("swapcase():", text4.swapcase())
	print("strip():", text5.strip())
	print("lstrip():", text5.lstrip())
	print("rstrip():", text5.rstrip())
	print("replace():", text6.replace("Java", "Python"))
	print("split():", text7.split())
	print("join():", "-".join(['a', 'b']))
	print("find():", text8.find("t"))
	print("index():", text8.index("t"))
	print("count():", text9.count("p"))
	print("startswith():", text8.startswith("py"))
	print("endswith():", text8.endswith("on"))
	print("isalpha():", text10.isalpha())
	print("isdigit():", text11.isdigit())
	print("isalnum():", text12.isalnum())
	print("islower():", text1.islower())
	print("isupper():", text2.isupper())
	print("isspace():", text13.isspace())
	print("center():", text1.center(10))
	print("ljust():", text1.ljust(10))
	print("rjust():", text1.rjust(10))
	print("zfill():", "5".zfill(3))
	print("partition():", text14.partition("-"))
	print("splitlines():", text15.splitlines())
	print("encode():", text16.encode())
	print("casefold():", text2.casefold())
	print("format():", "My name is {}".format("Riya"))
	
Output:
	upper(): PYTHON
	lower(): python
	title(): Hello World
	capitalize(): Python
	swapcase(): pYtHoN
	strip(): hi
	lstrip(): hi 
	rstrip():  hi
	replace(): I like Python
	split(): ['a', 'b', 'c']
	join(): a-b
	find(): 2
	index(): 2
	count(): 2
	startswith(): True
	endswith(): True
	isalpha(): True
	isdigit(): True
	isalnum(): True
	islower(): True
	isupper(): True
	isspace(): True
	center():   python  
	ljust(): python    
	rjust():     python
	zfill(): 005
	partition(): ('hello', '-', 'world')
	splitlines(): ['a', 'b']
	encode(): b'hello'
	casefold(): python
	format(): My name is Riya
	
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2.Basic operations: concatenation, repetition, string methods (upper(), lower(), etc.).
-->Basic String Operations in Python:
1. Concatenation:
- Concatenation means joining two or more strings using +.
Example:
	a = "Hello"
	b = "World"
	print(a + " " + b)
Output:
	Hello World
	
2. Repetition:
- Repetition means repeating a string using *.
Example:
	print("Hi " * 3)
Output:
	Hi Hi Hi

3. String Methods:
*upper():
- Converts string to uppercase.
Example:
	text = "python"
	print(text.upper())
Output:
	PYTHON
*lower():
- Converts string to lowercase.
Example:
	text = "PYTHON"
	print(text.lower())
Output:text = "python"

print(text.capitalize())
	python
*title():
- Converts first letter of each word to uppercase.
Example:
	text = "hello world"
	print(text.title())
Output:
	Hello World
*capitalize():
- Converts first letter to uppercase.
Example:
	text = "python"
	print(text.capitalize())
Output:
	Python
*swapcase():
- Changes uppercase to lowercase and lowercase to uppercase.
Example:
	text = "PyThOn"
	print(text.swapcase())
Output:
	pYtHoN
	
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. String slicing.
-->String Slicing in Python:
- String slicing is used to access a part of a string.
Syntax:
	string[start:end:step]
| Part    | Meaning                     |
| ------- | --------------------------- |
| `start` | Starting index              |
| `end`   | Ending index (not included) |
| `step`  | Jump between characters     |
Example:
	text = "Python"
| Character | P | y | t | h | o | n |
| --------- | - | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 | 5 |

->Basic Slicing:
Example:
	text = "Python"
	print(text[0:3])
Output:
	Pyt
	
->Slice from Middle:
Example:
	print(text[2:6])
Output:
	thon
	
->Omitting Start Index:
Example:
	print(text[:4])
Output:

String Slicing in Python:
- String slicing is used to access a part of a string.
Example:
	text = "Python"

Example 1: Basic slicing:
- Access characters from index 0 to 2
Example:
	print(text[0:3])
Output:
 	Pyt

Example 2: Slice from middle:
- Access characters from index 2 to 5
Example:
	print(text[2:6])
Output:
	thon

Example 3: Omitting start index:
- Starts from beginning automatically
Example:
	print(text[:4])
Output:
	Pyth

Example 4: Omitting end index:
- Goes till end automatically
Example:
	print(text[2:])
Output:
	thon

Example 5: Full string:
- Prints complete string
Example:
	print(text[:])
Output:
	Python

Example 6: Using step:
- Prints every 2nd character
Example:
	print(text[0:6:2])
Output:
	Pto

Example 7: Reverse string:
- Reverses the string using step -1
Example:
	print(text[::-1])
Output:
	nohtyP

Example 8: Negative index slicing:
Negative index starts from end
Example:
	print(text[-4:-1])
Output:
	tho

===================================================================================================================================================================================
