class Num:
    def __init__(self):
        self.num1=int(input("Enter Number 1 : "))
        self.num2=int(input("Enter Number 2 : "))

class Add(Num):
    def findSum(self):
        return self.num1+self.num2

class Sub(Num):
    def findDiff(self):
        return abs(self.num1-self.num2)
    

add=Add()
print("Sum : ",add.findSum())

sub=Sub()
print("Difference : ",sub.findDiff())
