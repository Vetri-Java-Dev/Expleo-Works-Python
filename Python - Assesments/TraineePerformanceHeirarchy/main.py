from SDETTrainee import SDETTrainee

name=input("Enter Name : ")
age=int(input("Enter Age : "))
email=input("Enter Email : ")

subjects=int(input("Enter no of subjects : "))
marks=[]

for i in range(subjects):
    marks.append(int(input(f"Enter Subject{i+1} Mark : ")))

batchId=int(input("Enter Batch ID : "))
noOfProjects=int(input("Enter no of projects : "))
noOfPublications=int(input("Enter no of publications : "))
tool=input("Enter tool proficiency : ")

#Object creation
trainee=SDETTrainee(name,age,email,batchId,marks,noOfProjects,noOfPublications,tool)

trainee.displayInfo()