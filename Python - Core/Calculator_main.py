from Calculator.Addition import add
from Calculator.Subtraction import sub
from Calculator.Multiplication import mul
from Calculator.Division import div,floorDiv

num1=int(input("Enter Number 1 : "))
num2=int(input("Enter Number 2 : "))

print("Addition : ",add(num1,num2))
print("Subtraction : ",sub(num1,num2))
print("Multiplication : ",mul(num1,num2))
print("Division : ",div(num1,num2))
print("Floor Division : ",floorDiv(num1,num2))