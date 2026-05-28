try:
    file=open("ExceptionHandling/greet.txt","w")

    try:
        file.write("Hello bruthaa !!!!")

    finally:
        file.close()
        print("File object closed")

except Exception as e:
    print(e)

finally:
    print("Finally block executed")