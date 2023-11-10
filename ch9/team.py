class Ally:
    """ally info, containing name and health"""
    
    def __init__(self, name, hp):
        """initialize attributes"""
        self.name = name
        self.hp = hp
        
    def ally_get_name(self):
        print(self.name)
        
    def ally_get_hp(self):
        print(self.hp)
        
class Enemy:
    """enemy info, containing name, health and coalition"""
    
    def __init__(self, name, hp, coalition):
        """initialize attributes"""
        self.name = name
        self.hp = hp
        self.coalition = coalition
        
    def enemy_get_name(self):
        print(self.name)
        
    def enemy_get_hp(self):
        print(self.hp)
        
    def enemy_get_coalition(self):
        print(self.coalition)
    
class Neutral:
    """Neutral character info"""
    
    def __init__(self, name):
        """initialize attribute"""
        self.name = name
        
    def ally_get_name(self):
        print(self.name)
