try:
    studentMarks={

        "25MCA001": 77,
        "25MCA009": 60,
        "25MCA025": 99,
        "25MCA007": 84,
        "25MCA012": 45,
        "25MCA021": 86,
        "25MCA032": 83,
        "25MCA018": 40,
        "25MCA014": 67

    }

    maxMarks=max(studentMarks.values())
    minMarks=min(studentMarks.values())

    print(f"Maximum : {maxMarks}->")

    for i in studentMarks:
        if(studentMarks[i]==maxMarks):
            print(i)

    print(f"Minimum : {minMarks}->")
    for i in studentMarks:
        if(studentMarks[i]==minMarks):
            print(i)

    distinction=[]
    merit=[]
    passed=[]
    fail=[]

    total=0

    for i in studentMarks:

        marks=studentMarks[i]
        total+=marks

        if marks>=86:
            distinction.append(i)

        elif marks>=76:
            merit.append(i)
        
        elif marks>=60:
            passed.append(i)
        
        else:
            fail.append(i)

    print(f"\nDistinction : {len(distinction)} : ",distinction)
    print(f"Merit : {len(merit)} : ",merit)
    print(f"Pass : {len(passed)} : ",passed)
    print(f"Fail : {len(fail)} : ",fail)

    print("\nClass Average :",round(total/len(studentMarks), 2))

    belowAverage=[]

    for i in studentMarks:
        if studentMarks[i]<(total/len(studentMarks)):
            belowAverage.append(i)

    print("Below Average : ", belowAverage)

    studentList=list(studentMarks.items())

    sorted(studentList,reverse=True)

    print("\n--- Leaderboard ---")
    for student in studentList:
        print(student[0],":",student[1])

except Exception as e:
    print("Error:", e)