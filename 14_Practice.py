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

