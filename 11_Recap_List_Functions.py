### *** List and Functions ***

## List accessing
n = [1, 3, 5]

# Print the second element 
print n[1]

# Change the second value
n[1] = 5 * n[1]
print n

# Append the number 4 here
n.append(4)
print n

## Removing elements from list 
# list.pop(index), list.remove(element), del(list[index]))

# Remove the first item in the list here
del(n[0])  # n.pop(0) or n.remove(1)
print n

## Changing the functionality of a functionality

# Ex 1
number = 5

# change the funtion to sum 3
def my_function(x):
  return x * 3
  
print my_function(number)

# Ex 2
m = 5
n = 13
# Add add_function here!
def add_function(x, y):
  return x + y

print add_function(m, n)

## Strings in functions
n = "Hello"
# Your function here!
def string_function(s):
  return s + "world"

print string_function(n)

## Passing a list to a function
def list_function(x):
  return x

n = [3, 5, 7]
print list_function(n)

## Using elements from list in a function
def first_item(items):
  print items[0]

numbers = [2, 7, 9]
first_item(numbers)

def list_function(x):
  return x[1]

n = [3, 5, 7]
print list_function(n)

## Modifiying elements of a list in a function
def double_first(n):
  n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
double_first(numbers)
print numbers

def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print list_function(n)

## List manipulation in functions

my_list = [1, 2, 3]
my_list.append(4)
print my_list
# prints [1, 2, 3, 4]

n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst

print list_extender(n)

## Printing out a list by item

n = [3, 5, 7]
  
def print_list(x):
  for i in range(0, len(x)):
  	print x[i]

print_list(n)

## Modifiying each element in a list with a function 

n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
# Don't forget to return your new list!

print double_list(n)

## Passing a range into a function (range() generates a range)
# range(stop) start = 0, range(start, stop) step = 1, range(start, stop, step)

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) # Add your range between the parentheses!

## Iterating over a list in function
# for item in list: (not able to modify the list)
#     print item

# for i in range(len(list)):  (you can modify the list)
#     print list[i]
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(len(numbers)):
    result = result + numbers[i]
  return result
print total(n)

## Using strings in lists in function

n = ["Michael", "Lieberman"]
# words argument is a list
def join_strings(words):
  # Empty string
  result = ""
  for i in range(len(words)):
    result = result + words[i]
  return result

print join_strings(n)

## Using to lists as arguments in a function
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  return x + y

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

## Using a list of lists in a function

# Ex 1:
list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:
  for item in lst:
    print item
    
# Ex 2:

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print flatten(n)
