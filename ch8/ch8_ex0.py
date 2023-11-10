#module, import, as, from, alias

#Function definitions are located in module ch8_ex_mod.py

#import module (file named ch8_ex_mod.py)
import Python.ch8_ex0_mod as ch8_ex0_mod

#also functions from a module can be imported with an asterisk:
# "from ch8_ex_mod import *"
# note: this can result in unexpected results, since the functions will be
# called without dot

#import a single function from a module
from ch8_mod import this_is_imported
#import multiple functions from a module
from ch8_mod import also_imported0, also_imported1
#giving an imported function an alias
from ch8_mod import this_long_function_name_will_be_given_an_alias_upon_import as func0

#A module can be imported and given an alias as well. For example the first import
# "import ch8_ex_mod" could instead be written "import ch8_ex_mod as mod8", 
# after which the below city_country(...) would be as followed:
# mod8.city_country(...)

#Call city_country() which prints the city-country arguments    
ch8_ex0_mod.city_country('berlin', 'germany')
ch8_ex0_mod.city_country('london', 'england')
ch8_ex0_mod.city_country('barcelona', 'spain')
print("\n")

#Call make_album() which returns a dictionary containing artist, album, (songs#)
work0 = {}
work1 = {}
work0 = ch8_ex0_mod.make_album('artist0', 'album0')
print(work0)
work1 = ch8_ex0_mod.make_album('artist1', 'album1', 12)
print(work1)
print("\n")

#Call make_album() in a loop using option to quit
prompt0 = 'Type artist: '
prompt1 = 'Type album: '
while True:
    input0 = input(prompt0)
    if input0 == 'q':
        break
    input1 = input(prompt1)
    if input1 == 'q':
        break
    print(ch8_ex0_mod.make_album(input0, input1))
print("\n")

#Calling and testing a single imported function from a module
this_is_imported()
also_imported0()
also_imported1()
#not_imported()
#>>> not defined

#below function has an alias name of a long function name in module ch8_mod.py
func0()

