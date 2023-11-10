class Machine:
    '''model machine frame'''
    def __init__(self, manuf, coo, secrecy_lvl):
        self.manuf = manuf
        self.coo = coo
        self.secrecy_lvl = secrecy_lvl
        
    def get_manufacturer(self):
        return self.manuf
    
    def get_country_of_origin(self):
        return self.coo
    
    def get_secrecy_lvl(self):
        return self.secrecy_lvl
    