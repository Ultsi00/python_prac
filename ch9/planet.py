class Terra:
    """Terra planet info: name and minerals"""
    
    def __init__(self, name, minerals):
        """initialize attributes"""
        self.name = name
        self.minerals = minerals

    def planet_get_name(self):
        return self.name
    
    def planet_get_minerals(self):
        return self.minerals
        
    def harvest_minerals(self, target):
        """reduces minerals from the target planet's mineral count"""
        harvest_amount = 3000
        self.minerals = self.minerals + harvest_amount
        target.minerals = target.minerals - harvest_amount
        

class Mars:
    """Mars planet info: name, minerals and danger level"""
    
    def __init__(self, name, minerals, danger_level):
        """initialize attributes. Contains default value 'age', ie. not in the arguments"""
        self.name = name
        self.minerals = minerals
        self.danger_level = danger_level
        self.age = '5 units'
        
    def planet_get_name(self):
        return self.name
    
    def planet_get_minerals(self):
        return self.minerals
        
    def planet_get_danger_lvl(self):
        """informs about planet's danger level (not used)"""
        print(self.danger_level)
    