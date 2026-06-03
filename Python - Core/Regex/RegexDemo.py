import re

string="Alan Turing was a pioneer of theoretical Turing computer science and ai. He was born on 23 june 1912 in maide, London"

result=re.search("^Alan.*London$",string)

if(result):
    print("We have a match.")
else:
    print("We dont have a match.")