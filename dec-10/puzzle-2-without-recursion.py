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


# Simulated the recursion behavior using stack (For this solution even recursion works, but for larger ones it might not work)
# For a particular location try to move in four directions if next cell value is in the sequence order
# If next cell value is 9 then increment paths count (both next value and next step should be 9)
def get_paths_iterative(start_x, start_y):
    stack = [(start_x, start_y)]  # Stack to keep track of current position
    paths = 0

    while stack:
        x, y = stack.pop()
        next_step = steps[steps.index(matrix[x][y]) + 1]  # Get next valid step

        for direction in DIRECTIONS:
            x1, y1 = x + direction[0], y + direction[1]
            if 0 <= x1 < row_length and 0 <= y1 < column_length:
                if matrix[x1][y1] == "9" and next_step == "9":
                    paths += 1
                elif matrix[x1][y1] == next_step:
                    stack.append((x1, y1))

    return paths


for x in range(row_length):
    for y in range(column_length):
        if matrix[x][y] == '0':
            starts.append((x, y))

total = 0
for start in starts:
    total += get_paths_iterative(start[0], start[1])

print(total)
