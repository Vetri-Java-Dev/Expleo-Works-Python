class Person:

    name=None
    age=None

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setName(self,name):
        self.name=name

    def setAge(self,age):
        self.age=age

person=Person("Vetri",21)

print("Name : ",person.name)
print("Age : ",person.age)

name=input("Enter name : ")
age=int(input("Enter age : "))

person.setName(name)
person.setAge(age)

print("Name : ",person.name)
print("Age : ",person.age)