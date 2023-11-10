#syntax:
# list = [], append(), insert(), del, pop(), remove(), sort(), sorted(), reverse(), reverse=True

#list
days = ['monday', 'friday', 'sunday'] #days will contain closed brackets
print(days)
days_parsed = f"{days}"
print(days_parsed.removesuffix(']').removeprefix('['))

print(days[0])
print(days[-1]) #accesses the last element of the list, can be -n. Error if list is empty
message = "today is "
print(f"{message}{days[2].title()}")

days[0] = 'tuesday' #modify an element in the list
print(days)
days.append('thursday')
print(days)

colours = []
colours.append('red')
colours.append('green')
print(colours)

colours.insert(0, 'blue') #inserts blue as element[0], and shifts the original (>=0)elements to right by one
print(colours)
del colours[2]  #del statement deletes the element at the pointed index value
print(colours)

items = ['chair', 'table', 'clock', 'phone']
items.pop()     #pop() method default index is the last
print(items)
item_popped = items.pop() #last is inserted to variable item_popped
print(item_popped)
items = ['chair', 'table', 'clock', 'phone']
item_popped = items.pop(1)
print(f"item_popped: {item_popped} | items: {items}")

numbers = {1, 2, 2, 2, 3, 4, 5}
print(numbers)
numbers.remove(2)   #remove() method removes all the elements equal to the argument
print(numbers)
wrong_nb = 3
numbers.remove(wrong_nb)
print(numbers)

cars = ['toyota', 'subaru', 'audi', 'datsun']
cars.sort()             #sorts the list into alphabetical order
print(cars)
cars.sort(reverse=True) #pass reverse=True as an arguement for sort() method
print(cars)
print(sorted(cars))     #sorted() method is a temporal sort. note sorted
print(cars)
cars.insert(1, "alfa_romeo")
cars.reverse()          #reverses list order (not alphabetically)
print(cars)
print(f"Car list lenght: {len(cars)}")






