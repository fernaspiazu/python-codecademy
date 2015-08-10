__author__ = 'fumandito'


def product(x):
    r = 0
    for i, n in enumerate(x):
        if i == 0:
            r = n
        else:
            r *= n

    return r


print product([4, 5, 5])
