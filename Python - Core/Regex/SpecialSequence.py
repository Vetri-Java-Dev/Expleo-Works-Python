import re

string="Alan Turing was a pioneer of theoretical Turing computer science and ai. He was born on 23 june 1912 in maide, London"

result=re.findall(r"\AAlan", string)
print("\\A (Starts with) : ", result)

result=re.findall(r"\bLon", string)
print("\\b Word boundary : ", result)

result=re.findall(r"\BLon", string)
print("\\B Not word boundary : ", result)

result=re.findall(r"\d", string)
print("\\d Digits : ", result)

result=re.findall(r"\D", string)
print("\\d Non Digits : ", result)

result=re.findall(r"\w", string)
print("\\w [A-B][a-b][0-9] and _ : ", result)

result=re.findall(r"\W", string)
print("\\W not [A-B][a-b][0-9] and _ : ", result)

result=re.findall(r"\s", string)
print("\\s space : ", result)

result=re.findall(r"\S", string)
print("\\S not space : ", result)

result=re.findall(r"London\Z", string)
print("\\Z Ends with : ", result)

