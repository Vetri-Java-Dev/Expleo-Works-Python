def isEven(num):
    return num%2==0

def sumOfOddAndEven(num):
    evenSum=0
    oddSum=0

    for i in range(num+1):
        if(isEven(i)):
            evenSum+=i
        else:
            oddSum+=i
    
    print("Even sum : ",evenSum)
    print("Odd sum : ",oddSum)

sumOfOddAndEven(20)