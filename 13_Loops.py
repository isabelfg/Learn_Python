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
for i in range(3):
