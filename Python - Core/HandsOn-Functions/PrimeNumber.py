import math

def isPrime(num):

    if(num<=1): return False

    for i in range(2,int(math.sqrt(num)+1),1):
        if(num%i==0):
            return False
    return True 

for i in range(1,100,1):
    if(isPrime(i)):
        print(i)