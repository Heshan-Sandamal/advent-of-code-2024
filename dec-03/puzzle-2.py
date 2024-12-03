import re

file = open("input.txt")
text = file.read()

# Regx to match multiple pattern mult(d,d) or do() or don't()
matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", text)

total = 0
enabled = True
for x in matches:
    if ("do()" == x):
        enabled = True
    elif ("don't()" == x):
        enabled = False

    if (enabled and "mul" in x):
        numbers = x.replace("mul(", "").replace(")", "").split(",")
        total += int(numbers[0]) * int(numbers[1])

print(total)
