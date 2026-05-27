string=input("Enter String : ")

special="!@#$%^*&_?><\\/"

for c in special:
    string=string.replace(c,"#")

print(string)
