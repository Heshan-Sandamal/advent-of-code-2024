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


# Check whether a particular update is valid or not
def is_valid(update):
    for x in range(len(update)):
        left, right = update[:x], update[x + 1:]
        val_dat = val_map[str(update[x])]
        for val in left:
            if (str(val) not in val_dat["before"]):
                return False

        for val in right:
            if (str(val) not in val_dat["after"]):
                return False
    return True


# Get invalid updates
invalid_list = []
for update in updates:
    if (not is_valid(update)):
        invalid_list.append(update)

# For each page in a particular update, check the created val_map that consists of items which should come before and after that item
# If the item in left side is not in the before list, switch the two elements and restart
# If the item in right side is not in the after list, switch the two elements and restart
total, index = 0, 0
while (index < len(invalid_list)):
    update = invalid_list[index]
    valid = True
    for x in range(len(update)):
        left, right = update[:x], update[x + 1:]
        val_dat = val_map[str(update[x])]

        temp = update[x]  # Keep item value temporary

        # Items on the left side
        for i in range(len(left)):
            if (str(left[i]) not in val_dat["before"]):
                # Switch values since those are not in a defined order
                update[x], update[x - len(left) - i] = left[i], temp
                valid = False
                break

        # Items on the right side
        for k in range(len(right)):
            if (str(right[k]) not in val_dat["after"]):
                # Switch values since those are not in a defined order
                update[x], update[x + 1 + k] = right[k], temp
                valid = False
                break

    # Only increment the current index if pages in the update is valid
    # Invalid means a switching of elements has happened
    # Then repeat from start until all elements are in the proper order
    if (valid):
        index += 1
        total += update[int(len(update) / 2)]

print(total)
