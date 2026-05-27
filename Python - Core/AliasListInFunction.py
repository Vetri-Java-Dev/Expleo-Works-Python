# def increment(listElement):

#     print(id(listElement))

#     for i in range(len(listElement)):
#         listElement[i]+=10

# integerList=[1,2,3,4,5,6]
# print(id(integerList))
# print(integerList)

# print("\n")

# increment(integerList)
# print(integerList)

def increment(listElement):

    listElement=[10,20,30,40,50,60]

    for i in range(len(listElement)):
        listElement[i]+=10
    
    print("List after increment : ",listElement)
    print("Id : ",id(listElement))


integerList=[1,2,3,4,5,6]
print("Id : ",id(integerList))

print("\n")

increment(integerList)

print(integerList)


    