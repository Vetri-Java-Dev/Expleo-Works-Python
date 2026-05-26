string="Hello world !! java1234556"

totalNumber=0;
totalLetter=0;
totalSymbol=0;

for s in string:
    if(s.isalpha()):
        totalLetter+=1

    elif(s.isnumeric()):
        totalNumber+=1
        
    else:
        totalSymbol+=1

print("Total no of letters : ",totalLetter)
print("Total no of numbers : ",totalNumber)
print("Total no of symbols : ",totalSymbol)