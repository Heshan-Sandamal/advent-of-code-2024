file = open("input.txt")
lines = file.read().splitlines()

# Actually there is no need to keep 2 lists, even one is enough, hence keep the before only to track of elements which come before an element
val_map = {}
updates = []
for line in lines:
    if ("|" in line):
        # Order Rules
        data = line.split("|")
        num1, num2 = data[0], data[1]

        # Set the list for each element which keep track of the elements
        if (num2 in val_map):
            val = val_map[num2]
            val.append(num1)
        else:
            val_map[num2] = [num1]

    elif ("," in line):
        # Pages in each update
        updates.append([int(i) for i in line.split(",")])

# For each page in a particular update, check the created val_map that consists of items which should come before
# Items in left should be in the list, and items in the right should not be in the list
total = 0
for update in updates:
    valid = True
    for x in range(len(update)):
        left, right = update[:x], update[x + 1:]
        for val in left:
            if (str(val) not in val_map[str(update[x])]):
                valid = False
                break

        for val in right:
            if (str(val) in val_map[str(update[x])]):
                valid = False
                break

    if (valid):
        total += update[int(len(update) / 2)]

print(total)
