integerList=list()

n=int(input("Enter the no of element : "))

for i in range(n):
    integerList.append(int(input(f"Enter {i+1}th number : ")))

print("Entered List : ",integerList)