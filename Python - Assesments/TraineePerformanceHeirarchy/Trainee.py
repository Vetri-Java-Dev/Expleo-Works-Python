from Person import Person

class Trainee(Person):
    def __init__(self,name,age,email,batchId,marks,numOfProject,noOfPublications):
        super().__init__(name,age,email)
        self.batchId=batchId
        self.marks=marks
        self.numOfProject=numOfProject
        self.noOfPublications=noOfPublications

    def displayInfo(self):
        super().displayInfo()
        print(f"Batch : {self.batchId}")
        print(f"Marks : {self.marks} | Average : {(sum(self.marks)/len(self.marks))}")
        print(f"Projects : {self.numOfProject} | Publications : {self.noOfPublications}")