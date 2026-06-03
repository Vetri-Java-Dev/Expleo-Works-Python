import re

string="Alan Turing was a pioneer of theoretical Turing computer science and ai. He was born on 23 june 1912 in maide, London"

result=re.search("Turing",string)

print("Group : ",result.group())
print("-"*30)

print("Starting Index : ",result.start())
print("-"*30)

print("Ending Index : ",result.end())
print("-"*30)

print("Span : ",result.span())
print("-"*30)

print("String : ",result.string)
print("-"*30)


                 