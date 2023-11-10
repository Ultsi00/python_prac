#Syntax:
#lower(), upper(), f""", title(), print, lstrip(), rstrip(), strip(), removeprefix(), removesuffix(), CONST

print("Hello")  # apostrophe can be used instead of quotation. The char which has a start and end, is identified
                # " 'hello' " >>> 'hello' / ' i like "cats" ' >>> i like "cats"
                
message = "this is variable"
print(message)

message = "previous message var overwritten"
print(message)

name0= "ada hill"
print(name0.title()) #title() method: each string literal convert to lowercase letter and their first letter to capital
name1 = "MICK stove"
print(name1.title())

name2 = "GARRY HILL"
print(name2.lower())    #lower() method: each string literal convert to lower case
name3 = "mary oven"
print(name3.upper())    #upper() method: each string literal convert to upper case

name4 = "mick"
name5 = "HiLL"
full_name0 = f"{name4} {name5}" #format string combines string variables
print(full_name0)
print(full_name0.title())
print(f"Hello {full_name0.title()}")
message1 = f"Hello {full_name0.upper()}"
print(message1)

print("\thello\nworld")

lwhitespace = "     lwhitespace"
rwhitespace = "rwhitespace     "
print(lwhitespace.lstrip()) #lstrip() method removes whitespaces from left side
print(rwhitespace.rstrip()) #rstrip() method removes whitespaces from right side
lwhitespace = lwhitespace.lstrip() #to remove whitespace permanently
print(lwhitespace)
lrwhitespace = "    left and right whitespace       \t   "
print(lrwhitespace.strip()) #strip() method removes whitespace from left and right

line = "first_middle_last"
print(line.removeprefix('first_'))
print(line.removesuffix('_last'))

print(2+2*3)
expo0 = 2 ** 4 #exponent are **
print(expo0)
underscore_nb = 1_000_000 #underscores are ignored within numbers, readability
print(underscore_nb)

CONST_EX0 = 5000        #constants are with capital letters
CONST_EX1 = "constant"
print(CONST_EX0)
print(CONST_EX1)







