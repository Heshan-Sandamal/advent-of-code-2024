file = open("input.txt")
text = file.read()
print(text)

num1 = [int(i) for i in list(text)]
file = []
id = 0
for i in range(len(num1)):
    if (i % 2 == 0):
        file += [str(id)] * num1[i]
        id += 1
    else:
        file += ["."] * num1[i]

total_blocks = sum([1 for x in file if x != "."])

end_index = len(file) - 1
blk_count = 0  # Keep track of different blocks

# Generate final format
# Looping from back and replacing dots with block numbers
final_blocks = []
for x in range(len(file)):
    char = file[x]
    if (char == "."):
        for y in range(end_index, 0, -1):
            end_char = file[y]
            if (end_char != "."):
                blk_count += 1
                file[x] = end_char
                end_index = y - 1
                final_blocks.append(end_char)
                break
    else:
        final_blocks.append(char)
        blk_count += 1

    if (blk_count == total_blocks):
        break

# Calculate total
total = 0
for x in range(len(final_blocks)):
    total += (x * int(final_blocks[x]))

print("total", total)
