__author__ = 'fumandito'


def median(numbers):
    _sorted = sorted(numbers)
    _length = len(_sorted)
    if _length % 2 == 0:  # if sorted list is even
        middle_index = _length / 2
        a = _sorted[middle_index - 1]
        b = _sorted[middle_index]
        return (a + b) / 2.0
    else:  # else it is odd
        index = (_length / 2.0) - 0.5
        return _sorted[int(index)]


print median([7, 3, 1, 4])
print median([7, 12, 3, 1, 6])
