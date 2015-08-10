__author__ = 'fumandito'


def reverse(text):
    s = ""
    i = len(text) - 1
    while i > -1:
        s += text[i]
        i -= 1
    return s


print reverse("ab#c!de@")
