__author__ = 'fumandito'


class Animal(object):
    """Makes cute Animals"""

    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age


hippo = Animal("Albert", 15)
hippo.description()

sloth = Animal("sloth", 10)
ocelot = Animal("ocelot", 5)

print hippo.health
print sloth.health
print ocelot.health
