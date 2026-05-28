def typeCheck(a , b=None):

    if(b is None):
        print(f"Single arguement : {a}")

    elif(isinstance(a, int) and isinstance(b, int)):
        print(f"{a} and {b} are Integers")

    elif(isinstance(a,str) and isinstance(b,str)):
        print(f"{a} and {b} are Strings")
    
    else:
        print("Mixed Types : {a},{b}")

#typeCheck(1)
typeCheck(1,2)
typeCheck("A","B")
typeCheck(1,"A")