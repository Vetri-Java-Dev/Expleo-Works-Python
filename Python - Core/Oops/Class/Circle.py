class Circle:

    radius=10
    color="Blue"

    def __init__(self, radius=1.0, color="White"):
        self.radius=radius
        self.color=color

    def getRadius(self):
        return self.radius
    
    def getColor(self):
        return self.color
    
    def setRadius(self, radius):
        self.radius=radius

    def setColor(self, color):
        self.color=color
    
    def getArea(self):
        return 3.14*(self.radius**2)
    
    #Class methods belongs to class 
    @classmethod
    def display(cls):
        print(f"Radius : {cls.radius} Area : {3.14*(cls.radius**2)} Color : {cls.color}")

    #like ToString() in java
    def __str__(self):
        return f"Radius : {self.radius} Area : {3.14*(pow(self.radius,2))} Color : {self.color}"

    
# circle=Circle(5.0,"Blue")
# print(circle)

# circle=Circle()
# print(circle)

# circle=Circle(11.0)
# print(circle)

Circle.display()

#Circle.setColor("Blue") Error

Circle.display()