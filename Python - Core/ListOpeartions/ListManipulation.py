integerList=list([1,2,3,4,5,6,7])

while(True):

    print("1.Append an element.")
    print("2.Append a list.")
    print("3.Modify an element")
    print("4.Insert an element.")
    print("5.Delete an element from position.")
    print("6.Delete an element based on value.")
    print("7.Sort list in ascending order.")
    print("8.Sort list in descending order.")
    print("9.Displaying the list")
    print("10.Exit")

    choice=int(input("Enter choice : "))

    match choice:
        case 1:
            integerList.append(input("Enter an element : "))

        case 2:
            tempList=list(map(int,input("Enter elements space seperated : ").split()))
            integerList.extend(tempList)
                
        case 3:
            index=int(input("Enter the position of an element to modify : "))
            modifiedElement=int(input("Enter modified element : "))
            integerList.pop(index)
            integerList.insert(index,modifiedElement)

        case 4:
            index=int(input("Enter the position of an element to be inserted : "))
            newElement=int(input("Enter element : "))
            integerList.insert(index,newElement)

        case 5:
            index=int(input("Enter index of an element to be deleted : "))
            integerList.pop(index)

        case 6:
            element=int(input("Enter element to be deleted : "))
            integerList.remove(element)

        case 7:
            integerList.sort()
            print("Sorted list (Ascending): ",integerList)

        case 8:
            integerList.sort(reverse=True)
            print("Sorted list (Descending) : ",integerList)

        case 9:
            print("List : ",integerList)
        case 10:
            break
        







    