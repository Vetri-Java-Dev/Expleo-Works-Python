greet="Welcome"

print("Traversal using for loop")
for i in greet:
    print(i)

print("Traversal using while loop")
index=0
while(index<len(greet)):
    print(greet[index])
    index+=1