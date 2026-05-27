text=input("Enter String : ")

lower=""
upper=""

for c in text:
    if(c.islower()):
        lower+=c
    else:
        upper+=c

result=lower+upper
print("Result : ",result)