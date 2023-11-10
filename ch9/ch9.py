#classes, class import syntax, instantiation, Inheritance, Composition


#importing a single class from a module
from cat import Cat

#importing multiple classes from a module
from team import Ally, Enemy

#importing the entire module
# in this manner, dot notation is required in instantiation:
# import cat -> cat_0 = cat.Cat(5, 'billie)
import planet

#family_member.py contains practice for inheritance
import family_member

#Try to avoid importing all classes from a module in the follow manner (can lead to issues difficult to diagnose):
# from <module> import *

#importing a parent from a module to a module, in which child/composition is located. Example:
# class Machine (parent) is located in machine.py
# class Cutter (child) is located in cutter.py
# class Engine (composition) is located in cutter.py (instance used as attribute for Cutter)
# syntax in cutter.py: from machine import Machine


#Instantiation: cat_0 = instance of a class
cat_0 = Cat(5, 'billie')
cat_1 = Cat(1, 'hinkie')

print(f"cat_0 name is {cat_0.name}, age is {cat_0.age}")
cat_0.sit()
cat_0.walk()
print(f"cat called {cat_1.name} is a kitten\n")


#Instantiation of different classes
ally_0 = Ally('Hank', 3000)
ally_1 = Ally('Frank', 2500)
enemy_0 = Enemy('Grok', 12400, 'warmongers')

if (ally_0.hp + ally_1.hp < enemy_0.hp):
    prompt = (f"enemy {enemy_0.name} has more health than {ally_0.name}\n")
    prompt += (f"and {ally_1.name} combined ({ally_0.hp} + {ally_1.hp} < {enemy_0.hp}).")
    print(f"{prompt}\n")

    
#Instantiation of classes after importing the entire module
home = planet.Terra('Terra', 5000)
target_0 = planet.Mars('Mars', 25000, 100)

print(f"{home.planet_get_name()}'s initial minerals: {home.planet_get_minerals()}")
print(f"{target_0.planet_get_name()}'s initial minerals: {target_0.planet_get_minerals()}")
print(f"{home.planet_get_name()} harvests minerals from {target_0.name}")
home.harvest_minerals(target_0)
print(f"{home.planet_get_name()}'s minerals after harvesting {home.planet_get_minerals()}")
print(f"{target_0.planet_get_name()}'s minerals after being harvested: {target_0.planet_get_minerals()}")
#accessing a default value in class Mars
print(f"Mars's age in : {target_0.age}\n")


#Inheritance
elder_0 = family_member.Parent('harrow', 'ronald')
offspring_0 = family_member.Child('harrow', 'kristie', 14)

print(f"elder name: {elder_0.get_family_name()}")
print(f"elder occupation: {elder_0.get_occupation()}")
print(f"elder bloodline: {elder_0.get_bloodline()}")
print(f"child name: {offspring_0.get_family_name()}")
print(f"child occupation: {offspring_0.get_occupation()}")  #parent-value overriden in child class
print(f"child bloodline: {offspring_0.get_bloodline()}")
print(f"child age: {offspring_0.get_age()}\n")


#Composition (instances as attributes)
print(f"child toy: {offspring_0.toy.get_toy_type()}")
print(f"toy value: {offspring_0.toy.get_price()}")
