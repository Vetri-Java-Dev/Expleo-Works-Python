with open("FileHandling/greet.txt","a+") as file:
    sentence=input("Enter Sentence : ")
    
    if(file.write(sentence)>0):
        print("Sentence wrote in file")
    else:
        print("File write failed")
    
    print(file.tell())
    file.seek(10,1)

    while True:
        line=file.readline()
        if(not line):
            break
        print(line)

