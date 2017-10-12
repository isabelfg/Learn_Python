## *** Date and Time ***

## The datetime library (print date and time in a nice format)

# Import the libray
from datetime import datetime

# Getting the current date (now())
now = datetime.now()
print now

# Extract information from date (year, month, day)
print now.year
print now.month
print now.day

# Format (yyyy-mm-dd or mm/dd/yyyy)
print '%s-%s-%s' % (now.year, now.month, now.day)
print '%s/%s/%s' % (now.month, now.day, now.year)

# Extract information from tine (HH:MM:SS)
print '%s:%s:%s' % (now.hour, now.minute, now.second)

# Recap
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
