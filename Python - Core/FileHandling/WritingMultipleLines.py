with open("FileHandling/greet.txt","w") as file:
    strings=["Hello Everyone !!\n","Good Evening\n","This is the last line\n"]
    print(file.writelines(strings))
