def calc(expression):
    operation=expression.split(" ")

    if(operation[0].casefold()=='Add'.casefold()):
        return int(operation[1])+int(operation[3])
    
    elif(operation[0].casefold()=='Subtract'.casefold()):
        return int(operation[1])-int(operation[3])
    
    elif(operation[0].casefold()=='Multiply'.casefold()):
        return int(operation[1])+int(operation[3])
    

expression=input("Enter your Expression : ")
print("Value : ",calc(expression))