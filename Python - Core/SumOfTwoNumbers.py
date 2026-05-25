firstNumber=int(input("Enter First number : "))
secondNumber=int(input("Enter Second number : "))

if(isinstance(firstNumber,int) and 
   isinstance(secondNumber,int)):
    print(f"The sum of {firstNumber} and {secondNumber} is : ",(firstNumber+secondNumber))

else:
    print("Input should be an Integer")