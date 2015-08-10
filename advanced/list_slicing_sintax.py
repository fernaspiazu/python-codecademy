__author__ = 'fumandito'

"""
List Slicing Syntax
Sometimes we only want part of a Python list.
Maybe we only want the first few elements; maybe we only want the last few.
Maybe we want every other element!

List slicing allows us to access elements of a list in a concise manner.
The syntax looks like this:

[start:end:stride]

Where start describes where the slice starts (inclusive),
end is where it ends (exclusive), and stride describes the space between items in the sliced list.
For example, a stride of 2 would select every other item from the original list to place in the sliced list.
"""

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]


# Print odd numbers
my_list = range(1, 11)
print my_list[::2]

backwards = my_list[::-1]
print backwards

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14]

print middle_third
