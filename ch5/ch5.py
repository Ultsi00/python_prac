#if, else, list scanning, boolean expressions, if-elif-else, empty list check, list combination

#if, else
fruits = ['apple', 'kiwi', 'orange']
for fruit in fruits:
    if fruit == 'kiwi':
        print(fruit.upper())
    else:
        print(fruit.lower())

nb_0 = 0
if nb_0 != 1:
    print("\nnb_0 is not 1\n")
else:
    print("\nnb_0 is 1\n")
    
nb_1 = 20
nb_2 = 30
if nb_1 >= 30 and nb_2 >= 30:       #another boolean operator "or" is used in the same manner
    print("both nbs are >= 30\n")
else:
    print("both nbs are not >= 30\n")

#Scanning through a list
letters = ['a', 'b', 'c', 'd']
if 'a' in letters:
    print(f"'a' is in the list\n")
if 'x' in letters:
    print(f"'x' is in the list\n")

users = ['john', 'bob', 'hillary', 'mark']
user_n = 'mark'
if {user_n} not in users:
    print(f"{user_n} is not in the list\n")
else:
    print(f"{user_n} is in the list\n")

#boolean expressions
day = 'monday'
print("is day monday?")
print(day == 'monday')
print("is day tuesday?")
print(day == 'tuesday')
word0 = 'HeLLo'
print(f"{word0.lower() == 'hello'}\n")

#if-elif-else
age = 15
if (age < 12):
    price = 0
elif (age < 18):    #valid only if the previous condition is false. condition check stops here
    price = 10
elif (age < 65):
    price = 20
else:
    price = 1
print(f"price: {price}\n")

#Empty list check
employees_working = []
if employees_working:
    for employee in employees_working:
        print(f"{employee} is working currently\n")
else:
    print(f"where is everyone?\n")

#list combination
users = ['bob', 'john', 'gary', 'hillary', 'helen', 'anthony']
users_banned = ['john', 'mick', 'helen']
print(f"Original user list: {users}")
for banned in users_banned:
    if banned in users:
        print(f"{banned} is banned. Removing from user list...")
        users.remove(banned)
    else:
        print(f"Scanning list further...")
print(f"Cleaned list: {users}\n")


        

