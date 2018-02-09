class Animal(object):
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def eat(self, amt):
        self.weight += amt
    def poop(self, amt):
        self.weight -= amt

class Cow(Animal):
    def moo(self, duration):
        return '{} says m{}!'.format(self.name, 'o' * duration)
    

class Chicken(Animal):
    def crow(self):
        return '{} likes to crow at the crack of dawn.'.format(self.name)

class Dog(Animal):
    def play(self):
        if self.age >= 10:
            duration = 5
        else:
            duration = 15
        return '{} is able to play for {} minutes.'.format(self.name, duration)
    
maximus = Dog('max', 10, 62)
print(maximus.play())

duke = Chicken('duke', 5, 7)
print(duke.crow())

bessie = Cow('bessie', 7, 1800)
print(bessie.moo(20))

bessie.eat(100)
bessie.poop(25)

print('{} weighs {} pounds.'.format(bessie.name, bessie.weight))