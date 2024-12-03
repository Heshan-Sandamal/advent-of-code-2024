import re

file = open("input.txt")
text = file.read()

# Regx to match pattern mul(d,d)
matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)

total = 0
for x in matches:
    numbers = x.replace("mul(", "").replace(")", "").split(",")
    total += int(numbers[0]) * int(numbers[1])

print(total)
