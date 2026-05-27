integerList=[1,2,3,4,5,6,7]
stringList=["A","B","C","D"]

integerList.sort()

print("Ascending (Integer list) : ",integerList)

integerList.sort(reverse=True)

print("Descending (Integer list) : ",integerList)

stringList.sort()

print("Ascending (String list) : ",stringList)

stringList.sort(reverse=True)

print("Descending (String list) : ",stringList)

#Using sorted()
print("Ascending : ",sorted(integerList))