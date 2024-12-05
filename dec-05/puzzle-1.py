file = open("input.txt")
lines = file.read().splitlines()

# Maintained two lists per element which keeps items which comes before and after particular item
val_map = {}
updates = []
for line in lines:
    if ("|" in line):
        # Order Rules
        data = line.split("|")
        num1, num2 = data[0], data[1]

        if (num1 in val_map):
            val = val_map[num1]
            val["after"].append(num2)
        else:
            val_map[num1] = {"before": [], "after": [num2]}

        if (num2 in val_map):
            val = val_map[num2]
            val["before"].append(num1)
        else:
            val_map[num2] = {"before": [num1], "after": []}

    elif ("," in line):
        # Pages in each update
        updates.append([int(i) for i in line.split(",")])

# For each page in a particular update, check the created val_map that consists of items which should come before and after that item
# The pages which are in left side of a particular page in a particular update, should be in the 'before' list
# The pages which are in right side of a particular page in a particular update, should be in the 'after' list
# If above two conditions are met, which mean that particular update has the pages in the defined order
total = 0
for page in updates:
    valid = True
    for x in range(len(page)):
        left, right = page[:x], page[x + 1:]
        val_dat = val_map[str(page[x])]
        for val in left:
            if (str(val) not in val_dat["before"]):
                valid = False
                break

        for val in right:
            if (str(val) not in val_dat["after"]):
                valid = False
                break
    if (valid):
        total += page[int(len(page) / 2)]

print(total)
