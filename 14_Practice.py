## *** Practice ***

## Function to kwon if a number is odd/even
def is_even(x):
  print "Is %s an even number?" %(x)
  if x % 2 == 0:
    return True
  else:
    return False

print is_even(6)
print is_even(11)

## Function to know if a number is integer
def is_int(x):
  print "Is %s and integer?" %(x)
  if x - round(x) == 0:
    return True
  else:
    return False

print is_int(7.0)
print is_int(7.5)
print is_int(-1)

## Sum of the digits of a number
def digit_sum(x):
    total = 0
    # round number for integer
    round(x)
    while x > 0:
      	# last digit = reminder(x/10)
        # total = total + last digit
        total += x % 10
        # Remove las digit
        # x = floor(x/10)
        x = x // 10
        print x
    return total
  
print digit_sum(1234)

## Calculate the factorial of int number
def factorial(x):
  total = 1
  while x > 1:
    total = total * x
    print total
    x = x - 1
    print x
  return total

num = 4
print "Factorial(%s): %s" %(num, factorial(num))

## Define if a number is prime or not
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

for num in range(12):
  if is_prime(num) == True:
    print "%s is a Prime number!" %(num)
  else:
    print "%s is not a Prime number!" %(num)
    
## Reverse a word
def reverse(text):
  # Empty string variable for reversed word
    word = ""
  # length of the original text for indexing
    l = len(text) - 1
  # Add the letters in reverse order
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
  
print reverse("world")

