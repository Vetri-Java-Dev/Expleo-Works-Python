num=int(input("Enter the number : "))

fact=1

if num<0:
    print("Factorial does not exist for negative numbers")

else:
    for i in range(1,num+1):
        fact=fact*i

print("Factorial : ",fact)