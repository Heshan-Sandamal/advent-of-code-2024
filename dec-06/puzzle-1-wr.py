with open("input.txt") as file:
    lines = file.read().splitlines()

grid = []
for line in lines:
    grid.append(list(line))

print(grid)
rows_length, columns_length = len(grid), len(grid[0])

# directions right = (0,1) , left = (0,-1) , up => (-1,0) , down -> (1,0)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West
row, column, direction = 0, 0, (-1, 0)

energized_tiles = set()

for x in range(rows_length):
    for k in range(columns_length):
        if grid[x][k] == '^':
            row = x
            column = k
            grid[x][k] = "."
            break

print(row, column)

# Iterative traversal of the grid

def traverse_iterative(row, column, direction):
    stack = [(row, column, direction)]  # Use a stack to simulate recursion

    while stack:
        current_row, current_column, current_direction = stack.pop()

        # Mark the current tile as energized
        energized_tiles.add((current_row, current_column))

        # Compute the next position
        next_row = current_row + current_direction[0]
        next_column = current_column + current_direction[1]

        if 0 <= next_row < rows_length and 0 <= next_column < columns_length:
            next_cell = grid[next_row][next_column]

            if next_cell == ".":
                # Move forward in the same direction
                stack.append((next_row, next_column, current_direction))
            elif next_cell == "#":
                # Turn right
                dir_index = DIRECTIONS.index(current_direction)
                new_dir_index = (dir_index + 1) % 4
                new_direction = DIRECTIONS[new_dir_index]

                new_row = current_row + new_direction[0]
                new_column = current_column + new_direction[1]

                if 0 <= new_row < rows_length and 0 <= new_column < columns_length:
                    stack.append((new_row, new_column, new_direction))

# Execute the traversal
traverse_iterative(row, column, (-1, 0))
print(len(energized_tiles))
