class Vehicle:

    def __init__(self, name, color, price):
        self.name=name
        self.color=color
        self.price=price
    
    def show(self):
        print(f"\nDetails :\nCar Name : {self.name}\nColor : {self.color}\nPrice : {self.price}\n")
    
    def maxSpeed(self):
        print("Vehicle max speed : 150")

    def changeGear(self):
        print("Vehicle gear changed")

class Car(Vehicle):

    def maxSpeed(self):
        super().maxSpeed()
        print("Car max speed : 300")
    
    def changeGear(self):
        print("Car gear changed\n")

car=Car("Verna","Black",100000)

car.show()
car.maxSpeed()
car.changeGear()

vehicle=Vehicle("Audi","White",1000)

vehicle.show()
vehicle.maxSpeed()
vehicle.changeGear()

print(Car.mro())
