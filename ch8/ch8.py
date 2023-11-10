#basic functions, key value arguments, Default value as function argument, special value None
# calling a function with a list (copy of a list), passing an arbitrary number of arguments (list),
# Arbitrary keyword arguments (dictionary)

#this practice does not use modules nor function import

#Function definitions:

def greet():
    """print Hello"""   #docstring = function purpose
    print("Hello")
    
def greet_user_info(name, age):
    print(f"Hello {name}, age {age}")
    
def greet_user_def(name, age='20'):
    print(f"Hello {name}, age {age}")
    
def get_person_name(id):
    name = ''
    if id == 0:
        name = 'boris_balkan'
    if id == 1:
        name = 'alexa_hill'
    return name
    
def get_person_dict(first_n, last_n, middle_n=''):
    if middle_n:
        person = {'first_name' : first_n, 'middle_name' : middle_n,
                  'last_name' : last_n}
    else:
        person = {'first_name' : first_n, 'last_name' : last_n}
    return person

def get_person_info(name, age=None):
    person = {'name' : name}
    if age:
        person['age'] = age
    return person

def modify_list(names_list):
    names_list[1] = 'IGOR'
    return names_list

def nb_list(*nbs):
    print(nbs)

def build_profile(first_n, last_n, **user_prof):
    user_prof['first_n'] = first_n
    user_prof['last_n'] = last_n
    return user_prof

    
####################################################################


#Testing functions:


#Basic function call    
i = 0
while i < 3:
    greet()
    i += 1
greet_user_info("adam", "15")

#Key value arguments: name-value pair 
greet_user_info(name='adam', age=15)

#Default value as function argument
greet_user_def('harry')             #>>>Hello harry, age 20
greet_user_def('harry', 15)         #overrides the default argument
greet_user_def('harry', age='15')   #overrides the default argument

#return value
full_name = get_person_name(1)
print(full_name)

#returning a dictionary (using an optional argument)
person = get_person_dict('hill', 'bob')
print(person)
person = get_person_dict('hill', 'bob', 'senior')
print(person)

#using a special value None
person = get_person_info('helen')
print(person)
person = get_person_info('helen', 22)
print(person)

#calling a function with a list (copy of a list)
names_list = ['tom', 'bob', 'hull']
names_list_new = []
print(f"Originals | names_list: {names_list} | names_list_new: {names_list_new}")
names_list_new = modify_list(names_list[:])
print(f"After function call | names_list: {names_list} | names_list_new: {names_list_new}")

#passing an arbitrary number of arguments: nb_list(*nbs)
#arbitrary arguments must be placed after positional arguments
nb_list(1)
nb_list(4, 2, 3)

#Arbitrary keyword arguments: build_profile(first_n, last_n, **user_prof)
#   ->  double asterisk creates a dictionary
#note: key-value pairs created with arbitr. kwargs are placed to the dictionary before positionally created pairs.
#   >>> {'age': '71', 'trade': 'marshall', 'status': 'deceased', 'first_n': 'glowen', 'last_n': 'harrow'}
user_info0 = build_profile('matt', 'brown')
print(user_info0)
user_info1 = build_profile('glowen', 'harrow', age='71', trade='marshall', status='deceased')
print(user_info1)
