#syntax:
#for, while, range(), min(), max(), sum(), List comprehension, slicing, list copying, tuple

colours = ['red', 'green', 'blue']
for colour in colours:
    print(colour)
#note that in print(<word>), <word> can be anything, as long as it matches "for <word> in colours"
print(colour)   #>>>blue    var colour contains the last value of for loop

days = ['monday', 'tuesday', 'friday']
i = 0
while i < len(days):
    print(days[i])
    i += 1

nbs = list(range(1, 4))     #>>> [1, 2, 3]
print(nbs)

for num0 in range(1, 5):    #>>> 1 2 3 4. note: will not print the last element (=5)
    print(num0)
for num1 in range(5):       #>>> 0 1 2 3 4
    print(num1)
even_nbs = list(range(0, 10, 2))    #third argument "2" is step. >>> 0, 2, 4, 6, 8. note: ignores value after the last step
print(even_nbs)

digits = [9, 4, 0, 2]
print(min(digits))
print(max(digits))
print(sum(digits))

#List comprehension:
squares0 = [sqr0**2 for sqr0 in range(1, 11)]
print(squares0)
#LC is the same as syntax below:
squares1 = []
for sqr1 in list(range(1, 11)):
    squares1.append(sqr1**2)
print(squares1)

#Slicing
players = ['mark', 'tom', 'jack', 'helene', 'andy']
print(players[0:2])     #>>> ['mark', 'tom'] | note: same as in range, last element not printed. See below interval
print(players[1:3])     #>>> ['tom', 'jack'] | note: like: "interval from 1 to 2, interval from 2 to 3"
print(players[:3])      #>>> ['mark', 'tom', 'jack'] | starts from 0: "intrv 0-1, intrv 1-2, intrv 2-3"
print(players[2:])      #>>> ['jack', 'helene', 'andy'] | "intrv 2-3, intrv 3-4, intrv 4-end"
print(players[-2:])     #>>> ['jack', 'helene', 'andy'] | from 2nd last to the end
print(players[:-4])     #>>> ['mark'] | from index0 to the beginning

for player in players[:4]:  #first 4 elements
    print(player.title())

#Copying List
my_objs = ['chair', 'table', 'lamp']
your_objs = my_objs[:]      #full list copy
his_objs = my_objs[1:]      #partial list copy
print(f"my objs: {my_objs}\nyour_objs: {your_objs}")
print(f"his_objs: {his_objs}")

#Tuple = list which cannot be changed. Declared with parentheses instead of closed brackets
const_list = (100, 200, 300)
print(const_list[1])
#const_list.append(3) >>> error
#modifying values in tuple requires reassigning the values to the list
const_list = (1, 2, 3)
print(const_list[1])
