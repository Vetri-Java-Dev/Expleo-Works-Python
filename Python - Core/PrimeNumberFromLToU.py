import math

start=int(input("Enter start : "))
end=int(input("Enter end : "))

if(start<end):
    for n in range(start,end+1):
        if(n>1):
            for i in range(2,int(math.sqrt(n)+1)):
                if(n%i==0):
                    break
            else:
                print(n,end=", ")

else:
    print("Invalid start and end")