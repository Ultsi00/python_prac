#Dictionary, Key-Value pair, adding and deleting pairs, Empty dictionary, Mofifying values, get(), 
# looping a dictionary, items(), accessing only keys/values, values(), set(), list of dictionaries
# dictionary in a dictionary

#Dictionary (Key : Value)
person_0 = {'age' : 20, 'name' : 'elron', 'nationality' : 'icelandic'}   #note braces instead of closed brackets in list declaration
print(person_0)
print(person_0['age'])
print(person_0['name'].upper())
print(f"He is {person_0['nationality']}\n")

#Adding values to a dictionary
person_0['preference'] = 'ice_cream'
person_0['hobby'] = 'hiking'
print(f"{person_0}\n")

#Empty dictionary
person_1 = {}
person_1['age'] = 30
person_1['name'] = 'bob'
print(f"{person_1}\n")

#Modifying values
person_1_old_name = person_1['name']
print(f"{person_1_old_name.title()}'s name yesterday: {person_1['name'].title()}.")
person_1['name'] = 'mary'
print(f"{person_1_old_name.title()}'s name today: {person_1['name'].title()}.\n")

#Deleting a key from a dictionary
print(f"Original person_1 dictionary: {person_1}")
del person_1['age']
print(f"person_1 dictionary after deletion: {person_1}\n")

#Declaring a longer dictionary than one row
food_selection = {
    'apple' : 2,
    'pear': 3,
    'banana' : 1,
    'kiwi' : 4,
    'tomato' : 1,
    'melon' : 3,
    'pineapple' : 3
    }

#using get() method to access a dictionary value
#the second argument _is not mandatory_. it is returned if the dictionary does not contain the variable,.
#this avoid an error.
obtained = food_selection.get('pear', "Not found")
not_found = food_selection.get('toyota', "Not found")
print(obtained)
print(not_found)
print("\n")

#Looping through a dictionary with key-value pairs, using items() method
car_0 = {'brand' : 'toyota', 'model' : 'old', 'price' : 1000}
for key, value in car_0.items():        #note: "key" & "value" can have random naming
    print(f"key: {key}")
    print(f"value: {value}")
print("\n")

fruits_0 = {'pear' : 5, 'apple' : 4, 'banana' : 2, 'orange' : 3}
for a, b in fruits_0.items():
    print(f"{a} costs {b}")
print(f"\n")

#Accessing only keys
for fruit in fruits_0:
    print({fruit})
print("\n")

#Accessing values associated with key
for fruit in fruits_0.keys():           #note: same output without keys() method
    print(f"is {fruit} affordable?")
    if fruits_0[fruit] < 4:
        price = fruits_0[fruit]
        print(f"{fruit} is affordable, it costs {price}")
    else:
        print(f"{fruit} is not affordable")
if 'potato' in fruits_0.keys():
    print(f"Potato should not be in fruits\n")
print("\n")
    
#Accessing values with values() method
total_cost = 0
for cost in fruits_0.values():
    total_cost = total_cost + cost
print(f"total cost of fruits: {total_cost}\n")

#using set() to skip repetitive values
nationalities = {
    'bob' : 'british', 
    'angela' : 'british',
    'boris' : 'russian',
    'tom' : 'slovakian',
    'frank' : 'american',
    'helen' : 'american'
    }
for nationality in set(nationalities.values()):
    print(nationality)

#List of dictionaries
print(f"\nelements list:")
elem_0 = {'shape' : 'round', 'feature' : ['hazardous', 'dynamic']}
elem_1 = {'shape' : 'square', 'feature' : ['stable', 'gigantic']}
elem_2 = {'shape' : 'round', 'feature' : ['volatile', 'passive']}
elements = [elem_0, elem_1, elem_2]
for elem in elements:
    print(elem)
print(f"elem_2 features:")
for feature in elem_2['feature']:
    print(f"\t{feature}")
print("\n")

#Dictionary in a dictionary
users = {
    'tstone' : {
        'first' : 'tom',
        'last' : 'stone'
    },
    'griver' : {
        'first' : 'gary',
        'last' : 'river'
    }
}
for username, name in users.items():
    print(f"username: {username} | first name: {name['first']} | last name: {name['last']}")
print("\n")


