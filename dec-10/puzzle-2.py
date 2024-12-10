file = open("input.txt")
lines = file.read().splitlines()

matrix = []
for line in lines:
    matrix.append(list(line.strip()))

# start locations
starts = []

row_length, column_length = len(matrix), len(matrix[0])

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West

# Valid step values sequence
steps = [str(x) for x in range(10)]


# For a particular location try to move in four directions if next cell value is in the sequence order
# If next cell value is 9 then terminate (both next value and next step should be 9)
# Instead of unique positions in part 1, used all_paths variables to find all paths that traversed to reach end point
def get_path(x, y):
    current = matrix[x][y]
    next_step = steps[steps.index(current) + 1]  # Get next valid step from the steps sequence Eg: if 1 -> 2, 2 -> 3

    all_paths = 0
    for direction in DIRECTIONS:
        (x1, y1) = (x + direction[0], y + direction[1])
        if 0 <= x1 < row_length and 0 <= y1 < column_length:

            if (matrix[x1][y1] == "9" and next_step == "9"):
                all_paths += 1
            elif (next_step == matrix[x1][y1]):
                all_paths += get_path(x1, y1)

    return all_paths


for x in range(row_length):
    for y in range(column_length):
        if (matrix[x][y] == '0'):
            starts.append((x, y))

total = 0
for start in starts:
    paths = get_path(start[0], start[1])
    total += paths

print(total)
