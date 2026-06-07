from DataValidator import validate_email, validate_phone, validate_usn, InvalidFieldError
from DataProcessor import process_email_data

n=int(input("Enter number of Trainee Records : "))

validRecords=[]

for i in range(n):

    print(f"\nEnter Record {i+1}")

    try:
        
        usn=input("Enter USN : ")
        name=input("Enter Name : ")
        email=input("Enter Email : ")
        phone=input("Enter Phone : ")

        validate_usn(usn)
        validate_email(email)
        validate_phone(phone)

        validRecords.append((usn, name, email, phone))

    except InvalidFieldError as e:
        print("ERROR : ", e)

processedRecords=process_email_data(tuple(validRecords))

print("Final Processed Records")
print("USN      Name      Username      Domain")

for record in processedRecords:

    usn=record[0]
    name=record[1]
    username=record[2]
    domain=record[3]

    print(usn,"\t",name,"\t",username,"\t",domain)