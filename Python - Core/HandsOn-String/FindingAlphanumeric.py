string=input("Enter String : ")

wordList=string.split(" ")

for word in wordList:
    hasDigit=False
    hasLetter=False

    for c in word:
        if(c.isalpha()):
            hasLetter=True
        elif(c.isnumeric()):
            hasDigit=True

    if(hasDigit and hasLetter):
            print(word)    