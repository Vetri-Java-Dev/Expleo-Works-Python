import re

string="Alan Turing was a pioneer of theoretical Turing computer science and ai. He was born on 23 june 1912 in maide, London"

print(re.sub("theoretical", "practical",string))

