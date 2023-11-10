#Current status of working employees and whether it is a weekday or not
is_weekday = True
employees_working = []
if employees_working:
    for employee in employees_working:
        print(f"{employee}")
    office_empty = False
else:
    print(f"Where is everyone?\n")
    office_empty = True

#Employee and vacation list comparison
employees = {'henry', 'john', 'laura', 'mark', 'andy', 'george', 'hillary'}
vacation = {'hillary', 'mark', 'andy'}
for employee in employees:
    if  employee not in vacation:
        employees_working.append(employee) 
    else:
        print(f"Scanning employee list further...")
print(f"These employees should be working: {employees_working}\n")

#Actions to take
if office_empty == True and is_weekday == True:
    print(f"Waking up CEO\n")
elif office_empty == True and is_weekday == False:
    print(f"False alarm\n")
elif office_empty == False and is_weekday == True:
    print(f"Nice\n")
else:
    print(f"Its weekend, note CEO to bring in a cake\n")
