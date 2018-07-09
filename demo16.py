class MyClass:
    """
       A simple example class
    """
    i = 12345
    def f(self):
        return 'hello world'
        
    def __init__(self):
        self.data = []

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)

class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x): 
        self.add(x)
        self.add(x)
    





    





