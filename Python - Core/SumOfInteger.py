n=int(input("Enter n : "));

i=1;
sum=0;

while(i<=n):
    num=int(input(f"Enter {i}th number : "))

    if(num==-1):break
    else : sum+=num

    i+=1
    
print("Sum : ",sum)
