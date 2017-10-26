### *** Loops ***

## While loop (while loop_condition:)
if count <= 9:
  print "Hello, I am an if statement and count is", count

while count <= 9:
  print "Hello, I am a while and count is", count
  count += 1
  
## Condition (loop_condition = True)
loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = Falsecount = 0

## Increment and arithmetic operations
num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  print num ** 2
  # Increment num (make sure to do this!)
  num += 1
  
## Simple errors
choice = raw_input('Enjoying the course? (y/n)')

# Fill in the condition (before the colon)
while choice != "y" and choice != "n":  
  choice = raw_input("I didn't catch that. Enter again: ")
  
## Infinite loops
count = 0

while count < 10: # Add a colon
  print count
  # Increment count
  count += 1

## Break the code (break statement exit the loop)
count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break

## While/else (else will execute loop_condition = false)
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"

# Ex 1:
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."

## Alternative for loop
print "Counting..."
for i in range(20):
  print i

## Repeat an action
hobbies = []
for num in range(3):
  hobby =  raw_input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)
print hobbies

## Print individual characters in a string
thing = "spam!"
for c in thing:
  print c

word = "eggs!"
for c in word:
  print c
  
## Print on the same line (, character)
phrase = "A bird in the hand..."
# Add your for loop
for char in phrase:
  if char == "A" or char =="a":
    print "X",
  else:
    print char,
#Don't delete this print statement!
print

## For loop with lists
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num

# Add your loop below!
for num in numbers:
  print num ** 2

## For loop with dictionary (get the key to the dictionary)
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == 10:
    print "This dictionary has the value 10!"

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
  print "%s %s" %(key, d[key])

## Indexing in the list (enumerate() gives index and item)
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item

## Multiple lists iteration (zip() gives pairs of elements of two lists)
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

# Print the larger of the two
for a, b in zip(list_a, list_b):
  if a >= b:
    print a
  else:
    print b

## For / else (else executed after for, if it ends normaly)
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

# else will always run without the break
print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    # break
  else:
  	print 'A', f
else:
  print 'A fine selection of fruits!'

## Recap
# Let's know each other
favorites = []

for num in range(3):
  favorite =  raw_input("Tell me one of your favorite actors: ")
  favorites.append(favorite)
print favorites

print 'Your favorite actors are...'
for f in favorites:
  if f == 'Penelope Cruz':
    print '%s is Beautiful!' % (f)
    # break
  else:
  	print 'I like %s!' % (f)
else:
  print 'I like them too!!'
