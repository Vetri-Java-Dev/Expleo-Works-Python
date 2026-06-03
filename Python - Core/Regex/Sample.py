import re 

pattern=r"\b\w+ing\b"

string="Walking and talking important."

result=re.search(pattern,string)
print("Search : ",result.group())

print("Find all : ",re.findall(pattern,string))