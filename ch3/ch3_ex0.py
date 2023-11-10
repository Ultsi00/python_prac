#original guest list
org_guests = ['matt', 'TOM', 'boris', 'helen', 'alexa']
print(f"Come to dinner: {org_guests}")

#reply
print(f"{org_guests[0].title()} cannot join")

#work on blacklist
print(f"insert {org_guests[0].title()} to blacklist")
blacklist = []
bl_person = org_guests.pop(0)
blacklist.append(bl_person)
print(f"blacklisted personnel: {blacklist}")
print(f"The CEO has to be blacklisted as well, at the top of the list")
blacklist.insert(0, 'David')
print(f"blacklisted personnel: {blacklist}")

#fix the current guest list
print(f"Current guest list: {org_guests}")
print("tom was invited accidentally, removing tom")
del org_guests[0]
print(f"Current guest list: {org_guests}")

#present guest list
org_guests.sort()
org_guests_parsed = f"{org_guests}"
org_guests_parsed = org_guests_parsed.removeprefix('[').removesuffix(']')
print(f"Final guest list ({len(org_guests)}  people): {org_guests_parsed}")
