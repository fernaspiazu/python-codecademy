__author__ = 'fumandito'

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}

print residents['Puffin']  # Prints Puffin's room number

# Your code here!
print residents["Sloth"]
print residents["Burmese Python"]


# key - animal_name : value - location
zoo_animals = {
    'Unicorn': 'Cotton Candy House',
    'Sloth': 'Rainforest Exhibit',
    'Bengal Tiger': 'Jungle House',
    'Atlantic Puffin': 'Arctic Exhibit',
    'Rockhopper Penguin': 'Arctic Exhibit'
}

# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"] = "Cos'e?"

print zoo_animals

inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
    'pocket': ['seashell', 'strange berry', 'lint'],
    'burlap bag': ['apple', 'small ruby', 'three-toed sloth']
}

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

print inventory
