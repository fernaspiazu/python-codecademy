__author__ = 'fumandito'


def is_int(x):
    return x == int(round(x, 0))


print is_int(7.0)  # True
print is_int(7.5)  # False
print is_int(-1)  # True
