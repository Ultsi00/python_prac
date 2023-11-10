#input(), dividing string to separate rows, typecast: int(), input in a loop, break/continue

text = input("write something: ")
print(text)

#dividing string to separate rows
prompt = "This is a longer message than PEP8 likes to have on one row.\n"
prompt += "Type input here: "
text = input(prompt)
print(text)

#typecast: int()
age = input("how old are you? ")
age = int(age)
print(age)

#input in a loop
message = ""
while message != 'quit':
    message = input('type "quit" to exit program, else type whatever ')

#break/continue
message = ""
while True:
    message = input('type "quit" to exit. type "1" to skip the prompt ')
    if message == 'quit':
        break
    if message == '1':
        continue
    else:
        print("this is the prompt message")
    
user_info = {}
prompt = "press ENTER to add another user. type 'quit' to print users and exit"
while True:
    first_name = input("Type first name: ")
    last_name = input("Type last name: ")
    user_info[first_name] = last_name
    selection = input(prompt)
    if selection == 'quit':
        break
print(user_info)
