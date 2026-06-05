class Person:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

    def displayInfo(self):
        print(f"Name : {self.name} | Age : {self.age}")

