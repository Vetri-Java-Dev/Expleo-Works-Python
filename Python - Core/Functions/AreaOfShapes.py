def areaOfSquare(side):
    return side**2

def areaOfRectangle(length,breadth):
    return length*breadth

def areaOfCircle(radius):
    return 3.14*(radius**2)

while True:
    print("1.Area of Circle ")
    print("2.Area of Square ")
    print("3.Area of Rectangle ")
    print("4.Exit")

    choice=int(input("Enter your choice : "))

    if(choice==1):
        radius=float(input("Enter radius : "))
        print(areaOfCircle(radius))

    elif(choice==2):
        side=float(input("Enter side : "))
        print(areaOfSquare(side))

    elif(choice==3):
        length=float(input("Enter length : "))
        breadth=float(input("Enter breadth : "))
        
        print(areaOfRectangle(length,breadth))

    elif(choice==4):
        print("Exiting")
        break

    else:
        print("Wrong choice")
