__author__ = 'fumandito'


def check_bit4(x):
    return "on" if 0b01000 & x > 0 else "off"


print check_bit4(0b100)

a = 0b10111011
mask = 0b100

print bin(a | mask)


"""
Using the XOR (^) operator is very useful for flipping bits.
Using ^ on a bit with the number one will return a result where that bit is flipped.

For example, let's say I want to flip all of the bits in a. I might do this:

a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1
"""
a = 0b11101110
mask = 0b11111111

print bin(a ^ mask)
