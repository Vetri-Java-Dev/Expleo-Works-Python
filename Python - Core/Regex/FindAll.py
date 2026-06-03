import re

string="Alan aTuringb was a pioneer of theoretical Turing computer science and ai. He was born on 23 june 1912 in maide, London"

print("Result of FindAll (Turing) : ",re.findall("Turing",string))

result=re.search("^Alan.*London$",string)

print("Span - (start, end) : ",result.span())