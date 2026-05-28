import traceback

try:
    n=int(input("Enter Number : "))
    if(n<=0):
        raise ValueError("This is either zero or negative")

except ValueError as e :
    print(e)
    traceback.print_exc()

else:
    print("Number is positive.")

finally:
    print("Succesfully handled")