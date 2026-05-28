def word(n):

    integerPair={
        "1":"One",
        "2":"Two",
        "3":"Three",
        "4":"Four",
        "5":"Five",
        "6":"Six",
        "7":"Seven",
        "8":"Eight",
        "9":"Nine",
        "0":"Zero"
    }
    
    result=""

    for c in n:
        result+=integerPair.get(c)+" "
    
    return result

n=input("Enter Number : ")
print(word(n))