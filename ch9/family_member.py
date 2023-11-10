class Parent:
    """"""
    def __init__(self, family_name, first_name):
        self.family_name = family_name

    def get_family_name(self):
        return self.family_name
    
    def get_occupation(self):
        return "carpenter"
        
    def get_bloodline(self):
        return "peasant"
    
# 1) child class must be in the same file with parent class, which must appear before the child,
#       unless parent is imported to a module, in which child is located
# 2) init() must contain atleast same arguments as parent (note: can contain more, <age> below)
# 3) a method in parent class can be overriden (see get_occupation())
# 4) super() function allows to call a method from parent class:
#       get_family_name(), get_occupation(), get_bloodline() are inherited to child class
# 5) composition: self.toy = Toy()
class Child(Parent):
    """simple model of a child class"""
    def __init__(self, family_name, first_name, age):
        super().__init__(family_name, first_name)
        self.age = age
        self.toy = Toy()
        
    def get_occupation(self):
        return "child is not occupied"
    
    def get_age(self):
        return self.age

#For composition (instance as attribute)
class Toy:
    def __init__(self, toy_type='teddy'):
        self.toy_type = toy_type
    
    def get_toy_type(self):
        return self.toy_type
    
    def get_price(self):
        if self.toy_type == 'teddy':
            return 'medium-priced'
        elif self.toy_type == 'hawk':
            return 'expensive'
        else:
            return 'affordable'

