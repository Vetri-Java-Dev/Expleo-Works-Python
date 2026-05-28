
class Person:

    def __init__(self, name, age):
        self.__name=name
        self.__age=age 
    
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name=name
    
    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        self.__age=age

#Inheritance 
class Employee(Person):
    pass

employee=Employee("Vetri",21)

print("Name : ",employee.getName())
print("Age : ",employee.getAge())

print("Value changed using setters")

employee.setName("Vetrivel")
employee.setAge(22)

print("Name : ",employee.getName())
print("Age : ",employee.getAge())

