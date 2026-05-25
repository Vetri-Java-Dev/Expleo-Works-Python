def maximum(*numbers):
    max=numbers[0]

    for n in numbers:
        if(n>max):
            max=n
    
    return max

print("Maximum among four integers : ",maximum(25,12,18,30))