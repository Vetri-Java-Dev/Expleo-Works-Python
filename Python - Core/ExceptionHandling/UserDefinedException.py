import traceback

class Error(Exception):
    pass

class ValueTooSmall(Error):
    pass

class ValueTooLarge(Error):
    pass


result=10

while(True):
    choice=int(input("Enter the number : "))

    try:
        if(choice==result):
            print("You won")
            break
    
        elif(choice<10):
            raise ValueTooSmall("Value you guessed is lower")
    
        elif(choice>10):
            raise ValueTooLarge("Value you guessed is higher")
    
    except Exception as e:
        print(e)
        traceback.print_exc()

    
    