__author__ = 'fumandito'


def is_numeric(num):
    return type(num) == int or type(num) == float


def distance_from_zero(num):
    return abs(num) if is_numeric(num) else "Nope"


print distance_from_zero(-20)
print distance_from_zero("fumandito")
