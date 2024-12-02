file = open("input.txt")
lines = file.read().splitlines()

total = 0
list1, list2 = [], []
for text in lines:
    values = text.split("   ")
    a, b = int(values[0]), int(values[1])
    list1.append(a)
    list2.append(b)

# Sort 2 lists
list1.sort()
list2.sort()

# Calculate distance of sorted lists
distance = 0
for x in range(len(list2)):
    distance += abs(list2[x] - list1[x])

print(distance)
