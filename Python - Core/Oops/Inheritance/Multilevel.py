class Student:

    def getStudentInfo(self):
        self.__rollno=input("Enter Roll no : ")
        self.__name=input("Enter Name : ")

    def displayStudentInfo(self):
        print("Student Name : ",self.__name)
        print("Student Roll no : ",self.__rollno)

class Marks(Student):

    def getMarks(self):
        self.__subject1=float(input("Enter mark of Subject 1 : "))
        self.__subject2=float(input("Enter mark of Subject 2 : "))
        self.__subject3=float(input("Enter mark of Subject 3 : "))
        self.__subject4=float(input("Enter mark of Subject 4 : "))
        self.__subject5=float(input("Enter mark of Subject 5 : "))

    def displayMarks(self):

        self.displayStudentInfo()

        print("Subject-1 Mark : ",self.__subject1)
        print("Subject-2 Mark : ",self.__subject2)
        print("Subject-3 Mark : ",self.__subject3)
        print("Subject-4 Mark : ",self.__subject4)
        print("Subject-5 Mark : ",self.__subject5)
    
    def getTotalMark(self):
        return self.__subject1+self.__subject2+self.__subject3+self.__subject4+self.__subject5

class Result(Marks):
    def getResult(self):
        return self.getTotalMark()
    
    def displayResult(self):
        self.displayStudentInfo()
        self.displayMarks()
        print(f"Result : {self.getResult()}/500")


result=Result()

result.getStudentInfo()
result.getMarks()
result.displayResult()


