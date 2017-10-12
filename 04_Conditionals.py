## *** Conditionals and Control Flow ***

## Control flow (choose among outcomes based on conditions)

# Example of control flow conditions
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

## Comparators (==, !=, <, <=, >, >=)

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 8 < 7

# Make me true!
bool_three = 2 >= 1

# Make me false!
bool_four = 6 < -4

# Make me true!
bool_five = 19 == 10 + 9

## Boolean operators (and, or, not)

"""
     Boolean Operators
------------------------      
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

## AND

# False and False
bool_one = False

# -(-(-(-2))) == -2 and 4 >= 16 ** 0.5
bool_two = False

# 19 % 4 != 300 / 10 / 10 and False
bool_three = False

# -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2
bool_four = True

# True and True
bool_five = True

## OR

# 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'
bool_one = False

# True or False
bool_two = True

# 100 ** 0.5 >= 50 or False
bool_three = False

# True or True
bool_four =  True

# 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1
bool_five = True

## NOT

# not True
bool_one = False

# not 3 ** 4 < 4 ** 3
bool_two = True

# not 10 % 3 <= 10 % 2
bool_three = True

# not 3 ** 2 + 4 ** 2 != 5 ** 2
bool_four = True

# not not False
bool_five = False


## Order of evaluation ((), not, and, or)

# False or not True and True
bool_one = False

# False and not True or True
bool_two = True

# True and not (False or False)
bool_three = True

# not not True or False and not True
bool_four = True

# False or not (True and True) 
bool_five = False

## Make some examples of true or false

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = (10 == (9+1)) or (2 > 3)

# Make me false!
bool_three = (6 == 4) and (2 > 0)

# Make me true!
bool_four = not not True

# Make me true!
bool_five = not (-4 > -1)

## Conditional Statement Syntax (IF True then execute)

# Will the print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.
response = "Y"

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"

# True conditons for if statements
def using_control_once():
    if 8 > 2:
        return "Success #1"

def using_control_again():
    if 10 > 1:
        return "Success #2"

print using_control_once()
print using_control_again()


