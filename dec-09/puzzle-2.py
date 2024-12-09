file = open("input.txt")
text = file.read()

disk_map = [int(i) for i in list(text)]

file = []
id = 0
# Generate the blocks map using the input numbers
for i in range(len(disk_map)):
    if (i % 2 == 0):
        file += [str(id)] * disk_map[i]
        id += 1
    else:
        file += ["."] * disk_map[i]

# Count for different blocks
total_blocks = sum([1 for x in file if x != "."])

# IDs of blocks sorted from descending order
ids = set(file)
ids.remove(("."))
ids = [str(t) for t in sorted([int(x) for x in ids], reverse=True)]

# Store information on blocks
block_infos = []
for x in ids:
    block_infos.append({
        "id": x,
        "count": file.count(x),
        "index": file.index(x)
    })

# For each block try to replace free spaces starting the largest block
# Per each file block, check from start of the blocks map see whether free spaces are less than size of the file block
for blocks in block_infos:
    char = ""
    spaces = []
    sp_start = False # Is free space block
    sp_start_index = -1 # Starting index of the free space block

    for x in range(blocks["index"] + 1):
        char = file[x]
        # identify start of dot
        if (char == "." and (sp_start == False)):
            sp_start = True
            sp_start_index = x
            spaces.append(".")
            x += 1
        elif (char == "." and (sp_start == True)):
            # rest of the dots
            spaces.append(".")
            x += 1
        elif (sp_start == True and char != "."):
            # end of the free spaces (dots) block
            # Now we can check whether the file block can be moved to free spaces
            space_length = len(spaces)  # length of free space block

            # Check whether the block can be fitted to the spaces, if so update the spaces -> block and block -> dots
            if (space_length >= blocks["count"]):
                for t in range(0, blocks["count"]):
                    file[sp_start_index + t] = blocks["id"]
                    file[blocks["index"] + t] = "."
                break

            # End of the space block
            spaces = []
            sp_start = False

# Calculate total
total = 0
for x in range(len(file)):
    if (file[x] != "."):
        total += (x * int(file[x]))

print(total)
