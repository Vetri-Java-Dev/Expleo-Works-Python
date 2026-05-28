with open("FileHandling/greet.txt","r") as file:
    stringList=file.readlines()
    
    for sentence in stringList:
        word=sentence.splitlines()
        print(word)
