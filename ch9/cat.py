#By convention, capitalized names in Python refer to classes
# Functions part of a class are called methods

class Cat:
    """A simple class to represent a cat"""
    
    def __init__(self, age, name):
        """initialize attributes"""
        self.age = age
        self.name = name
    
    def sit(self):
         print(f"A cat called {self.name} is sitting.")
    
    def walk(self):
        print(f"A cat called {self.name} is walking.")
        
