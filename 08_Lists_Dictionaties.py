### *** Lists and Dictionaries***

## Lists (datatype to store different pieces of info under a variable)

# List example (list_name = [item_1, item_2] or empty_list = [])
zoo_animals = ["pangolin", "cassowary", "sloth", "wolf"];

if len(zoo_animals) > 3:
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]
  
# Access by index (list_name[index], starting by 0)
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

# Reassigning [list_name[index] = new value)
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]

zoo_animals[2] = "hyena"
zoo_animals[3] = "wolf"

# Not fixed length (list_name.append[element])
suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("umbrella")
suitcase.append("sunscreen")
suitcase.append("hat")

list_length = len(suitcase)

print "There are %d items in the suitcase." % (list_length)
print suitcase

# List Slicing (new_list = list_name[index1 : index2])
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]
# Third and fourth items (index two and three)
middle = suitcase[2:4]
# The last two items (index four and five)
last =  suitcase[4:6]

# Slicing strings as lists (list_name[:2] of list_name[3:])
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]
# The fourth through sixth characters
dog = animals[3:6]
# From the seventh character to the end
frog = animals[6:]

# Search for index (list_name.index("string"))
# Insert items in the list (list_name.insert(index, "string"))
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

# Use index() to find "duck"
duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")
print animals

# For loop with a list (for variable in list_name...)
my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
  print 2 * number

# Sort lists (list_name.sort())
start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
	square_list.append(x**2)
  
# if you indent the next line it will be in the loop  
square_list.sort()
print square_list

# Remove from a list (list_name.remove(element))
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")

## Dictionary (list with "key" index = string or number)
# d = {'key1' : 1, 'key2' : 2, 'key3' : 3} or empty_d = {}
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number
print residents["Sloth"]
print residents["Burmese Python"]

# New entries (dict_name[new_key] = new_value)
# You can put lists inside dictionaries
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu["Paella"] = 13.20
menu["Cocido"] = 10.35
menu["Tortilla de patata"] = 9.30

print "There are " + str(len(menu)) + " items on the menu."
print menu

# Remove items (del dic_name[key_name])
# key - animal_name : value - location (multiple lines)
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]

zoo_animals["Rockhopper Penguin"] = "Artic Exhibit"
print zoo_animals

# Access to content (dic_name[key][index])
# Example 1:
my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]

# Example 2:
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] += 50

print inventory









