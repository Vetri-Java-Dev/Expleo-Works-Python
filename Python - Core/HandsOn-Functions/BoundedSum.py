def isEven(num):
    return num%2==0

def sumOfOdd(lowerBound,upperBound):
    oddSum=0
    for i in range(lowerBound,upperBound+1):
        if(not isEven(i)):
            oddSum+=i
    
    return oddSum

def sumOfEven(lowerBound,upperBound):
    evenSum=0
    for i in range(lowerBound,upperBound+1):
        if(isEven(i)):
            evenSum+=i
    
    return evenSum

lowerBound=int(input("Lower Bound : "))
upperBound=int(input("Upper Bound : "))

evenSum=sumOfEven(lowerBound,upperBound)
oddSum=sumOfOdd(lowerBound,upperBound)

print("Even sum : ",evenSum)
print("Odd sum : ",oddSum)

print("Absolute difference : ",abs(evenSum-oddSum))

