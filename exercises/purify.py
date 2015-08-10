__author__ = 'fumandito'


def purify(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list


print purify([1, 2, 3])
