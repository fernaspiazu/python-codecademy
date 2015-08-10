__author__ = 'fumandito'

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first = suitcase[:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last = suitcase[4:]  # The last two items (index four and five)

print suitcase
print first
print middle
print last

animals = "catdogfrog"
cat = animals[:3]  # The first three characters of animals
dog = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]  # From the seventh character to the end

print cat
print dog
print frog

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")  # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")

print animals  # Observe what prints after the insert operation
