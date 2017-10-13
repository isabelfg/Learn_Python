## *** Functions: Reusable piece of code ***

## Tip and tax calculator with functions

def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

## Function components (header, comments, body)

# Header: def name_function(parameter1, parameter2,...)
# Comments: "What the function does"
# Body: Idented conditional statemens

def hello_world():
  """Prints 'Hello World!' to the console."""
  print "Hello World!"

# Call to a function
hello_world()

# Example: Function that calculates the square of a number
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
  
# Call the square function! Make sure to
# include the number 10 between the parentheses.
square(10)

## Parameters and arguments

def power(base,exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!

## Functions calling functions

def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2
  
# Example: To the cube and by three

def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

## Importing functions (a library, a function, everything)

# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)

# Import *just* the sqrt function from math on line 3!
from math import sqrt
print sqrt(25)

# Import *everything* from the math module on line 3!
# Be aware of the problems of rename the functions with same name
# as the ones in the modules
from math import *

# Show all the avaiblable functions in math module
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!

## Built in functions (no module inport)

def biggest_number(*args):
  print max(args)
  return max(args)
    
def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# Maximum value max()
# Set maximum to the max value of any set of numbers
maximum = max(1,2,3)
print maximum


# Minimum value min()
# Set maximum to the max value of any set of numbers
minimum = min(1,2,3)
print minimum

# Absolute value abs() Distance from 0
# absolute = abs(-42)
print absolute

# Type of the data type()
# Print out the types of an integer, a float and string
print type(42)
print type(4.2)
print type('spam')

## Recap

# Define a function
def shut_down(s):
  if s == "yes":
  		return "Shutting down"
  elif s == "no":
  		return "Shutdown aborted"
  else:
      return "Sorry"

# Import sqrt and use it
from math import sqrt
print sqrt(13689)

# Built in functions
def distance_from_zero(number):
  if type(number) == int or type(number) == float:
    return abs(number)
  else:
    return "Nope"
 

