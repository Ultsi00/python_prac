#Creating a number list
list_nbs0 = list(range(0, 30))  #0-29
print(f"{list_nbs0}\n")

#Using while to add numbers to a list
list_nbs1 = []
i = 0
while i <= 10:
    list_nbs1.append(i)
    i = i + 1
print(f"nbs 0 - 10: {list_nbs1}\n")

#Creating a number list of squares using List comprehension
list_sqrs = [(sqr**2) for sqr in range(0, 10)]
print(f"{list_sqrs}\n")

#Creating a number list of squares without List comprehension
list_sqrs1 = []
for sqr1 in list(range(0, 10)):  #0-9 
    list_sqrs1.append(sqr1**2)
print(f"{list_sqrs1}\n")

#Creating two lists: even and odd numbers, using step as the third argument in range()
list_even = list(range(0, 30, 2))
print(list_even)
list_odd = list(range(1, 31, 2))
print(f"{list_odd}\n")

#Min, max, sum
print(f"Sum even numbers: {sum(list_even)}")
print(f"Odd numbers: min = {min(list_odd)}, max = {max(list_odd)}\n")

#Slicing a list
fruits = ['apple', 'kiwi', 'pear', 'orange', 'banana', 'tomato', 'lemon']
print(fruits[:2])   #>>> ['apple', 'kiwi']
print(fruits[1:3])  #>>> ['kiwi', 'pear']
print(fruits[:])    #>>> ['apple', 'kiwi', 'pear', 'orange', 'banana', 'tomato', 'lemon']
print(fruits[3:])   #>>> ['orange', 'banana', 'tomato', 'lemon']
print(fruits[:-2])  #>>> ['apple', 'kiwi', 'pear', 'orange', 'banana'
print(fruits[-3:])  #>>> ['banana', 'tomato', 'lemon']

#Copying a list
print(f"\n")
list_org = [1 ,2, 3]
list_cpy = list_org[:]
print(f"list org: {list_org} | list_cpy: {list_cpy}")
#Partial copy
list_cpy = list_org[:2]
print(f"partial list_cpy: {list_cpy}\n")

#Tuple: declaration in (parentheses) instead of [closed brackets]
cars = ('datsun', 'lada', 'toyota', 'jeep')
#cars.remove() >>> error    #tuple modification only via re-assigning
cars = ('datsun', 'lada', 'bmw', 'jeep', 'jaguar')
print(cars)

