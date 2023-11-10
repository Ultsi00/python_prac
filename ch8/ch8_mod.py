#This module is used to practice importing selected functions, not the entire module
#Function(s) will be imported to ch8_ex0.py

def this_is_imported():
    prompt = 'This is a separate function, imported from ch8_mod.py\n'
    prompt += 'the other function "not_imported()" will not be imported.'
    print(prompt)
    
def not_imported():
    print("not imported")
    
def also_imported0():
    print("also imported0")
    
def also_imported1():
    print("also imported1")
    
def this_long_function_name_will_be_given_an_alias_upon_import():
    print("this function was given an alias 'func0'")
    

