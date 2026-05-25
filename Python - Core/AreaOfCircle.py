PI=3.14159

radius=int(input("Enter Radius : "))

if(radius>=0):
    print("Area of the Circle : ",round(PI*(radius**2),5))
else:
    print("Radius should be positive.")