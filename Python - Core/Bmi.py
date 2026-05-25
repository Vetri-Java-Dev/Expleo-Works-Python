weight=float(input("Enter you Weight(kg) : "))
height=float(input("Enter your Height(Ms) : "))

bmi=None

if(weight<=0 or height<=0):
    pass
else:
    bmi=(weight/(height**2))

print("Bmi : ",round(bmi,2))