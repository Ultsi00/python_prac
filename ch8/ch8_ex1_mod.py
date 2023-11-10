#This module is imported to ch8_ex1.py

def craft_sandwich(*fillings):
    """fillings is string(s), which are printed"""
    print(fillings)
    
def build_profile(first, last, **info):
    info['first'] = first
    info['last'] = last
    return info
    