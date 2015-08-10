__author__ = 'fumandito'


def factorial(x):
    return 1 if x in range(2) else x * factorial(x - 1)


print factorial(0)
