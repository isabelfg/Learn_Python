## *** Strings and Console output ***

## Strings (letter, numbers and symbols)

# Set the variable brian on line 3!
brian = "Hello life!"

# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"

print caesar
print praline
print viking

## Escaping characters (\)

# The string below is broken. Fix it using the escape backslash!
'This isn\'t flying, this is falling with style!'

## Acces by index (string characters assigned to a number = index)

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "PYTHON"[4]
print fifth_letter

## String Methonds (len, lower, upper, str)

# Lenght of the string
parrot = "Norwegian Blue"
print len(parrot)

# Get rid of the capitalization in the string
parrot = "Norwegian Blue"
print parrot.lower()

# Capitalize the string
parrot = "norwegian blue"
print parrot.upper()

# Turn no strings into strings

"""Declare and assign your variable on line 4,
then call your method on line 5!"""
pi = 3.14
print str(pi)

## Dot notation len(parrot) / parrot.upper()
# Methods that use dot notation only work with strings
# len() and str() can work with other data types

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

## Printing strings (from editor to console)

# Tell Python to print "Monty Python"
print "Monty Python"

## Printing variables

# Assign the string "Ping!" to the variable the_machine_goes and print it
the_machine_goes = "Ping!"
print the_machine_goes

## Stromg Concatenation (with +)

# Print the concatenation of "Spam and eggs"
print "Spam " + "and " + "eggs"

## Explicit string conversion (combine string and no strings with str())

# Turn 3.14 into a string
print "The value of pi is around " + str(3.14)

## String formating (print variable with a string %s)

# Une variable
name = "Mike"
print "Hello %s" % (name)

# Two variables
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

# Several %s
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

## Recap

my_string = "Freedom for women!"
print len(my_string)
print my_string.upper()
print "What we want is: %s" % (my_string)
