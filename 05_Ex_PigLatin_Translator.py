## *** Pig Latin Translator *** ##

# Program that ask for an english word
# Put the first letter at the end
# and add sufix "ay" to the word

print 'Welcome to the Pyg Latin Translator!'

# Variables
pyg = "ay"

# Enter a word in English
original = raw_input("Enter a word: ")

# Check if there is something inside original
# Check that the word contain alphabetic char
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print 'empty'
