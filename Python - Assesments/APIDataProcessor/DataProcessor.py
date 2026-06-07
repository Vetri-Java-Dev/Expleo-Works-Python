def accept_trainee_records():

    n=int(input("Enter number of trainees : "))

    records=()
    tempList=[]

    for i in range(n):

        print("\nEnter Trainee Details")

        usn=input("Enter USN : ")
        name=input("Enter Name : ")
        email=input("Enter Email : ")
        phone=input("Enter Phone : ")
        
        tempList.append((usn, name, email, phone))

    records=tuple(tempList)

    return records

def process_email_data(records):
    processedList=[]

    for record in records:

        usn=record[0]
        name=record[1]
        email=record[2]
        phone=record[3]

        parts=email.split("@")
        username=parts[0]
        domain=parts[1]

        processedList.append((usn, name, username, domain))

    return tuple(processedList)