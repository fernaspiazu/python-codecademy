__author__ = 'fumandito'

my_list = range(1, 16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda f: f == "Python", languages)

squares = [x ** 2 for x in range(1, 11)]
print filter(lambda f: 30 <= f <= 70, squares)
