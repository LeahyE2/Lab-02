import re

pattern = r"\d+\.\d+\.\d+\.\d+"

text = "Failed login from 192.168.0.1 at 10:30"
text2 = "Failed login from 10.0.0.5 at 10:30"

answer = text + text2  # for concatonation assign a new value to the concatonated values
print(re.findall(pattern,answer))


