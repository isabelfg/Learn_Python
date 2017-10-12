## *** Basic level Python (www.codeacademy.com) ***

print "Welcome to Python!

## Python Syntax: Variables (numbers)

# Write your code below!
my_variable = 10

# Write your code above!
print my_variable

## Python Syntax: Data Types (integer, float, booleans (True, False))

# Set the variables to the values listed in the instructions!
my_int = 7
my_float = 1.23
my_bool = True

# Write your code above!
print my_int
print my_float
print my_bool

## Python Syntax: Reassign values

# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?
my_int = 7

# Change the value of my_int to 3 on line 8!
my_int = 3

# Here's some code that will print my_int to the console:
# The print keyword will be covered in detail soon!
print my_int

## Python Syntax: Whitespaces (structure the code with indentations)

# Bad Format
def spam():
eggs = 12
return eggs
        
print spam()

# Good Format(two spaces of indentation)
def spam():
  eggs = 12
  return eggs
        
print spam()

## Python Syntax: Interpreter (runs the code and check for errors)

# Declare some variables for the interpreter to read
spam = True
eggs = False

## Python Syntax: Single line comments (#)

# Define the meaning of the universe
mysterious_variable = 42

## Python Syntax: Multi-line comments (triple quotation """ bla """)

""" This is the only 
good answer to every problem:
I was drunk
"""

## Python Syntax: Math (+, -, *, /, exponent **, modulo %)

# Set count_to equal to the sum of two big numbers
count_to = 2345 + 8320
print count_to

# Set eggs equal to 100 using exponentiation on line 3!
eggs = 10 ** 2
print eggs

# Modulo operator returns reminder from a division
# Set spam equal to 1 using modulo on line 3!
spam = 10 % 3
print spam

## Python Syntax: All together

# Basic Python all together
monty = True
python = 1.234
monty_python = python ** 2

## Exercise : Tip Calculator
# Cost of meal = 44.50$
# Restaruant Tax = 6.75%
# Tip = 15%

# Assign the variable meal the value 44.50 on line 3!
meal = 44.50

# tax and tip variables are the decimal value of 6.75 an 15
tax = 6.75 / 100

# Reassign meal value to meal with taxes
meal = meal + meal * tax

# Include the tax
total = meal + meal * tip

# Write the result of meal in the interpreter
print("%.2f" % total)








