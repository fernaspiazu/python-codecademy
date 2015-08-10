__author__ = 'fumandito'


def digit_sum(n):
    total = 0
    if n < 1:
        print "Error"
    else:
        for number in str(n):
            total += int(number)
    return total


print digit_sum(1234)
