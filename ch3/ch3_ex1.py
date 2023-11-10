#Create a list of 10 states (not in an alphabetical order)
states = ['atlanta', 'georgia', 'illinois', 'iowa', 'florida', 'texas', 
          'new_york', 'ohio', 'tennessee', 'michigan', 'colorado']

#Count states
states_cnt = len(states)

#Print list, '\n' between elements
i = 0
print("States:")
while i < states_cnt:
    print(f"\t{states[i].title()}")
    i += 1              #increment(++)/decrement(--) operator not part of syntax

#Print as raw python list
print(f"original raw list:\n{states}\n")

#Print alphabetically sorted raw list, without modifying the original order
print(f"alphabetically sorted raw list:\n{sorted(states)}\n")

#Print alphabetically reverse sorted raw list, without modifying the original order
print("alphabetically reverse sorted raw list: ")
print(sorted(states, reverse=True))

#Print as original raw list
print(f"\noriginal raw list:\n{states}\n")

#Reverse the order of the list (non-alphabetically)
states.reverse()
print(f"reversed raw list (non-alphabetically):\n{states}\n")

#Sort the list alphabetically
states.sort()
print(f"alphabetically sorted raw list:\n{states}\n")

#Alphabetical reverse sorted raw list
states.sort(reverse=True)
print(f"alphabetically reverse sorted raw list:\n{states}\n")

#List modifications
#Remove all "new_york" elements
to_rm = 'new_york'
states.remove(to_rm)
#Move the last element to a variable
state_rdm = states.pop(-1)
#Delete 3rd element from the list
del states[2]
#Replace the former 3rd element with a new state
states.insert(2, "maryland")
#Append an element to the end of the list
states.append('delaware')

#Print final raw list
print(f"Final raw list after secret modifications:\n{states}")
