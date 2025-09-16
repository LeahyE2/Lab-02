import re

pattern = r"ar"
text ="the char of the car set alarm bells ringing."

matches = re.findall(pattern, text)
print(matches)

