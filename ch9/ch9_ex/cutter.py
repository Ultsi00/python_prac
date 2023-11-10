from machine import Machine

class Cutter(Machine):
    '''model cutter details: target and cost depend on secrecy_lvl
        and energy type'''
    def __init__(self, manuf, coo, secrecy_lvl, energy_type, cost):
        super().__init__(manuf, coo, secrecy_lvl)
        self.energy_type = energy_type
        if self.energy_type == 'electric':
            self.secrecy_lvl = 'private'
            self.cost = cost + Battery(self.secrecy_lvl).get_battery_cost()
        else:
            self.cost = cost + Battery(self.secrecy_lvl).get_battery_cost()
        
    def get_target(self):
        if self.secrecy_lvl == 'private':
            return 'sewer network'
        else:
            return 'shoreline projects'
    
    def get_energy_type(self):
        return self.energy_type
        
    def get_cost(self):
        return self.cost
    
class Battery:
    '''battery cost is dependant on cutter secrecy_lvl'''
    def __init__(self, secrecy):
        self.secrecy = secrecy    
    
    def get_battery_cost(self):
        if self.secrecy == 'private':
            return 3200
        else:
            return 500
