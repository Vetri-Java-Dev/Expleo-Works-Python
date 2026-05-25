name=input("Enter your Name : ")
age=int(input("Enter your Age : "))
color=input("Enter your Favourite Color : ")

if(age>=0 and age<=150):
    if(len(name)<=255 and len(color)<=255):
        print("Name : ",name)
        print("Age : ",age)
        print("Favorite Color : ",color)
else:
    print("Invalid data")
    

