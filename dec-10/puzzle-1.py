file = open("input.txt")
lines = file.read().splitlines()

matrix = []
for line in lines:
    matrix.append(list(line.strip()))

# start locations
starts = []

row_length, column_length = len(matrix), len(matrix[0])

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West

# Valid step values
steps = [str(x) for x in range(10)]


# For a particular location try to move in four directions if next cell value is in the sequence order
# If next cell value is 9 then terminate
# positions set contains the unique end locations reached
def get_path(x, y):
    current = matrix[x][y]
    next_step = steps[steps.index(current) + 1] # Get next valid step from the steps sequence Eg: if 1 -> 2, 2 -> 3
    positions = set()

    for direction in DIRECTIONS:
        (x1, y1) = (x + direction[0], y + direction[1])
        if 0 <= x1 < row_length and 0 <= y1 < column_length:

            if (next_step == "9" and matrix[x1][y1] == next_step):
                positions.add((x1, y1))

            elif (next_step == matrix[x1][y1]):
                positions1 = get_path(x1, y1)
                positions.update(positions1)

    return positions


for x in range(row_length):
    for y in range(column_length):
        if (matrix[x][y] == '0'):
            starts.append((x, y))

# Per each starting point traverse through the matrix until 9 is found
total = 0
for start in starts:
    all_positions = get_path(start[0], start[1])
    total += len(all_positions)

print(total)
