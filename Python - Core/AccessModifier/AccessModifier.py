# age-> public
# __age-> private
# _age-> protected

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

person=Person("Vetri",21)

print("Name : ",person.getName())
print("Age : ",person.getAge())

print("Value changed using setters")

person.setName("Vetrivel")
person.setAge(22)

print("Name : ",person.getName())
print("Age : ",person.getAge())

