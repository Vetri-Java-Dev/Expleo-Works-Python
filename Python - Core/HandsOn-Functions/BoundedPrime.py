import math

def isPrime(num):
    if(num<=1): return False
    for i in range(2,int(math.sqrt(num)+1),1):
        if(num%i==0):
            return False
    return True 

lowerBound=int(input("Lower Bound : "))
upperBound=int(input("Upper Bound : "))

for i in range(lowerBound,upperBound+1):
    if(isPrime(i)):
        print(i)