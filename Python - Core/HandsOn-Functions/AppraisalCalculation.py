def newSalary(salary,rating):
    if(rating<=0):
        return salary
    elif(rating<=4):
        return salary+(salary*(0.10))
    elif(rating<=7):
        return salary+(salary*(0.25))
    elif(rating<=10):
        return salary+(salary*(0.30))

salary=float(input("Enter your Salary : "))
rating=float(input("Enter you Appraisal Rating : "))

print("New Salary :",int(newSalary(salary,rating)))

