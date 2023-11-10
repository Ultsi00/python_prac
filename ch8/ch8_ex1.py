import ch8_ex1_mod as m

#calling a function in module
m.craft_sandwich('tomato', 'ham', 'onion')
m.craft_sandwich('sauce', 'shrimps')
m.craft_sandwich('lettuce', 'mayonese', 'onion', 'kebab')

#build a profile: first name, last name, arbitrary amount of characteristics
prof0 = {}
prof0 = m.build_profile(
    'gary', 'maine', age='young', status='employed', trade='fisherman')
print(prof0)
