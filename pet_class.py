'''
class Dog(object):
    # Class Attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
'''

class Pet():

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

# Parent class
class Dog(object):
# Class attribute
    species = 'mammal'
    is_hungry = True
# Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
# instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
# instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    def walk(self):
        return "{} is walking!".format(self.name)        
    def eat(self):
        self.is_hungry = False
# child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
# child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

maximus = Dog('max', 10)
roscoe = RussellTerrier('roscoe', 22)
brutus = Bulldog('brutus', 4)
drew = Dog('drew', 15)

roscoe.eat()
        
my_dogs = [maximus, roscoe, brutus, drew]

my_pet = Pet(my_dogs)

string = ''

string += 'I have {} dogs. '.format(len(my_pet.dogs))

all_hungry = True

for dog in my_pet.dogs:
    string += '{} is {}. '.format(dog.name, dog.age)
    if not dog.is_hungry:
        all_hungry = False
    

string += "And they're all {}s, of course. ".format(Dog.species)

if all_hungry:
    string += 'My dogs are hungry.'
else:
    string += 'My dogs are not hungry.'

print(string)

my_pet.walk()