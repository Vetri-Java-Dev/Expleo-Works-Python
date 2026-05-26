string="Hello, world!"

# if("el" in string):
#     print("Contains")
# else:
#     print("Not contains")

# #replacing char 
# newString="j"+string[6:]
# print(newString)

# new="j"+string[-6:-1]
# print(new)

# W  E  L  C  O  M  E
# -7 -6 -5 -4 -3 -2 -1

greet="helloWorld"

print(greet.lower())
print(greet.upper())
print(greet.find('lo'))
print("banana".find("na",3))

greet=greet.replace("world","Vetri")
print(greet)

print(greet.capitalize())
print(greet.count("e"))
print("isAlpha : ",greet.isalpha())
print("isNumeric : ",greet.isnumeric())

print("Startswith 'Hell' : ",greet.startswith("hell"))
print("Ends with 'rld' : ",greet.endswith("rld"))

