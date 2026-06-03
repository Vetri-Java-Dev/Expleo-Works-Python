import re

pattern=r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}\b"

textWithEmail="Contact me at bvetrivel@gmail.com or employee1735@gmail.com"

print(re.findall(pattern,textWithEmail))