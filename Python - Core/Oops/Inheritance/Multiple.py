class TeamMember:

    def __init__(self, name, id):
        self.name=name
        self.id=id

    def display(self):
        print(f"Name : {self.name}\nId : {self.id}")


class Worker:

    def __init__(self, pay, jobTitle):
        self.pay=pay
        self.jobTitle=jobTitle

    def display(self):
        print(f"Pay : {self.pay}\nJob Title : {self.jobTitle}")


class TeamLeader(TeamMember, Worker):

    def __init__(self, name, id, pay, jobTitle, exp):
        TeamMember.__init__(self, name, id)
        Worker.__init__(self, pay, jobTitle)
        self.exp = exp

    def display(self):
        TeamMember.display(self)
        Worker.display(self)
        print("Experience : ", self.exp)


teamLeader=TeamLeader("Vetri", 161, 30000, "Tester", 1)
teamLeader.display()