from datetime import datetime

today=datetime.now().year

bday=input("Enter you DOB (YYYY-MM-DD) : ")
bdayYear=int(bday[0:4])

print("Age : ",(today-bdayYear))
