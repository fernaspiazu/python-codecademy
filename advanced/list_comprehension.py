__author__ = 'fumandito'

# Create list with even numbers from 0 to 50
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# even_squares list should include the squares of the even numbers between 1 to 11.
# Your list should start [4, 16, 36...] and go from there.
even_squares = [x ** 2 for x in range(1, 12) if (x ** 2) % 2 == 0]
print even_squares


# The comprehension should consist of the cubes of the numbers 1 through 10
# only if the cube is evenly divisible by four.
cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print cubes_by_four
