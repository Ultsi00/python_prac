#Program prompts for the user’s favorite number. Uses json.dumps() to store this number in a file. 
# If the number is already stored, user is informed that the exact number exists in the file.
# Prints the old (different) number in the file, or the new (same) number.

#**errors:
# - not protected against empty .json file
# - tested only with .json content: "<number>", "<char>"
# - not protected against non-existing ex0.json

from pathlib import Path
import json
from numbers import Number

def exit_message(number):
    msg_fav_nr = "Your favorite number is: "
    print(msg_fav_nr + number) 

def get_path():
    '''returns a pre-set relative path'''
    '''not protected against errors**'''
    path = Path("ex0.json")
    return path
    
def set_fav_nr():
    '''requests a number'''
    prompt = "Enter favorite number: "
    nr_fav0 = input(prompt)
    return nr_fav0

def get_fav_nr():
    '''gets the favorite number from .json'''
    content = get_path().read_text()
    number = json.loads(content)
    return number

def write_json():
    '''writes the content in .json'''
    content = json.dumps(nr_new.get_value())
    get_path().write_text(content)  


nr_old = Number(get_fav_nr())
nr_new = Number(set_fav_nr())

if nr_old.get_value() == nr_new.get_value():
    print("same number exists in file")
else:
    print(f"old number was: {nr_old.get_value()}")
    write_json()
exit_message(nr_new.get_value())
