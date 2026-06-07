import re

try:

    with open(r"LogFileAnalyser\server_log.txt","r") as file:
        content=file.read()

    lines=content.splitlines()

    totalLines=len(lines)
    totalWords=0
    totalChars=len(content)
    totalVowels=0

    infoCount=0
    warningCount=0
    errorCount=0
    criticalCount=0

    alerts=[]

    for line in lines:

        words=line.split()
        totalWords+=len(words)

        for ch in line:
            if(ch.lower() in "aeiou"):
                totalVowels+=1

        levels=re.findall(r"\[(INFO|WARNING|ERROR|CRITICAL)\]",line)

        for level in levels:

            if(level=="INFO"):
                infoCount+=1

            elif(level=="WARNING"):
                warningCount+=1

            elif(level=="ERROR"):
                errorCount+=1
                alerts.append(line)

            elif(level=="CRITICAL"):
                criticalCount+=1
                alerts.append(line)

    with open("log_report.txt", "w") as file:

        file.write(f"Total Lines : {totalLines}\n")
        file.write(f"Total Words : {totalWords}\n")
        file.write(f"Total Chars : {totalChars}\n")
        file.write(f"Total Vowels : {totalVowels}\n\n")

        file.write(f"INFO : {infoCount} WARNING : {warningCount} ERROR : {errorCount} CRITICAL:{criticalCount}\n\n")

        file.write("--- ALERTS ---\n")

        for alert in alerts:
            file.write(alert+"\n")

    print("Report generated successfully")

except FileNotFoundError:
    print("server_log.txt not found")

except Exception as e:
    print("Error :",e)

finally:
    print("File processing completed")