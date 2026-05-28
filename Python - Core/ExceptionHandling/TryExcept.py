try:
    a=int(input("Num 1 : "))
    b=int(input("Num 2 : "))
    c=a/b

    print("Division : ",c)

except(ZeroDivisionError):
    print("Zero division is impossible")
else:
    print("Manipulated without exception.")
finally:
    print("Completed computing")