### *** Supermarket ***

# for loop list
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for element in names:
	print element

# for loop dictionary
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}
# Add your code below!
for key in webster:
	print webster[key]
  
# for and if loops
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
  if number % 2 == 0:
    print a[number]

# List + functions

# Ex 1:
def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total

lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print small

# Ex 2:
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
    	count = count + 1
  return count

print fizz_count(["fizz", "cat", "fizz"])

# String looping
for letter in "Codecademy":
  print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print letter

# Your own store
# Dictionary for prices
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}

# Dictionary for stock
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

# Print inventory
for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]

# Total money if you sell everything
total = 0
for key in prices:
  value = prices[key] * stock[key]
  print value
  total += value
print total

# Online Shop
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total = total + prices[item]
      stock[item] = stock[item] - 1
  return total

print compute_bill(shopping_list)
