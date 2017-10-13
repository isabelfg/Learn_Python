## *** Example for Functions ***

# What is a function?
def answer():
  return 42

# Define a function that calculates the cost of the vacations
# Calculate hotel cost
def hotel_cost(nights):
  return 140 * nights

# Calculate the plane ride 
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

# Calculate cost of transportation
def rental_car_cost(days):
  cost_day = 40
  if days >= 7:
    return cost_day * days - 50
  elif days >= 3:
    return cost_day * days - 20
  else:
    return cost_day * days

# Pull it together
def trip_cost(city, days, spending_money):
  a = rental_car_cost(days)
  b = plane_ride_cost(city)
  c = hotel_cost(days)
  return a + b + c + spending_money

print trip_cost("Los Angeles", 5, 600)


  
