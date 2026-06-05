from Trainee import Trainee

class SDETTrainee(Trainee):
    
    def __init__(self,name,age,email,batchId,marks,noOfProjects,noOfPublications,tool):
        super().__init__(name,age,email,batchId,marks,noOfProjects,noOfPublications)
        self.tool=tool
    
    #(avg_marks × 0.6) + (num_projects × 5) + (num_publications × 3)

    def displayInfo(self):
        super().displayInfo()
        print(f"Tool : {self.tool}")
        print("Aggregate Score :",((sum(self.marks))/len(self.marks))*0.6+(self.numOfProject*5)+(self.noOfPublications*3))