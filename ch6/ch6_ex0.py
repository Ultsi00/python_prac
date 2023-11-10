#Create two dictionaries, each dictionary containing two dictionaries. Add dictionaries into a list.
#Print the full list
people = []
upper = {
    'bob' : {
        'info_0' : 'sheriff',
        'info_1' : 'middle-aged'
    },
    'helen' : {
        'info_0' : 'mayor',
        'info_1' : 'bilingual'
    }
}
lower = {
    'nick' : { 
        'info_0' : 'convict', 
        'info_1' : 'trilingual'
    },
    'gary' : { 
        'info_0' : 'hunter',
        'info_1' : 'outlaw'
    }
}
people = [upper, lower]
print(f"people full raw data:\n{people}\n")

#Create pet dictionaries, which contain owner's name and pet type. Add dictionaries into a list.
#Loop the list and print the list elements.
#Print only the pet type
pet0 = {'owner' : 'gary', 'type' : 'dog'}
pet1 = {'owner' : 'bob', 'type' : 'bird'}
pet2 = {'owner' : 'nick', 'type' : 'cat'}
pets = [pet0, pet1, pet2]

for pet in pets:
    print(pet)

for pet in pets:
    print(pet['type'])
    if pet['owner'] == 'bob':
        print(f"Didnt know bob had a pet ({pet['type']}).")
print("\n")

#Create a dictionary of users and their 'lucky' numbers.
#Loop the dictionary and print out the names and the numbers.
users = {
    'kat' : ['1', '5'],
    'bob' : ['8', '9'],
    'tom' : ['1', '4']
}
for name, nbs in users.items():
    nb0 = nbs[0]
    nb1 = nbs[1]
    print(f"{name}'s lucky numbers are: {nb0} and {nb1}")
#Can write: f"{name}'s lucky numbers are: {nbs}", 
#but output will contain [' and '], as list doesn't have attribute .removeprefix() / .removesuffix()
print("\n")

#Use variables (name0...) as keys in a dictionary. Nest information dictionaries into these keys.
#Information dictionaries have their own key-value pair: key = country, value = score.
#Use .values() to sum up scores.
name0 = 'paris'
name1 = 'london'
name2 = 'berlin'
cities = {
    name0 : {
    'country' : 'france',
    'score' : 2000  
    },
    name1 : {
    'country' : 'england',
    'score' : 3000 
    },
    name2 : {
    'country' : 'germany',
    'score' : 700  
    }
}
for city, info in cities.items():
    print(f"{city} is located in {info['country']}, with a score of {info['score']}")

scores_tot = 0
for info in cities.values():        #refers to values in braces after "name0" key
    scores_tot += info['score']
print(f"total score: {scores_tot}\n")

#Extend a dictionary by adding a new key-value pair. 
#Change a value of a key.
info0 = {'shape' : 'round', 'value' : 'medium'}
info0['rarity'] = 'common'
info0['shape'] = 'square'
print("keys and their values: ")
for key, value in info0.items():    #without .items() => ValueError: too many values to unpack (expected 2)
    print(f"\t{key}\t| {value}")
    