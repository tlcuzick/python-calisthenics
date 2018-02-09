class Dog(object):
    # Class Attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
maximus = Dog('Max', 10)
drew = Dog('Drew', 12)
brodee = Dog('Brodee', 4)
        
def get_biggest_number(*args):
    oldest = 0
    for a in args:
        if a.age > oldest:
            oldest = a.age
    print('The oldest dog is {} years old.'.format(oldest))
    
get_biggest_number(maximus, drew, brodee)