class DemoClass:

    n=10

    def demo(self):
        for i in range(10):
            print(i,end=" ")
    
    def display(hi):
        for i in range(10):
            print(i,end=" ")
        

obj=DemoClass()

print("Behaviour : ")

obj.display()

print("\nState : ",obj.n)
