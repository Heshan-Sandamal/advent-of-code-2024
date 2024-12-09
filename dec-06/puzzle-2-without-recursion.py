with open("input.txt") as file:
    lines = file.read().splitlines()

grid = []
for line in lines:
    grid.append(list(line))

rows_length, columns_length = len(grid), len(grid[0])
# directions right = (0,1) , left = (0,-1) , up => (-1,0) , down -> (1,0)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West
row, column, direction = 0, 0, (-1, 0)

visited_cells = set()

for x in range(rows_length):
    for k in range(columns_length):
        if grid[x][k] == '^':
            row = x
            column = k
            grid[x][k] = "."
            break

print("Start Location: ",row, column)


# Since recursion exceeds the limit, replaced recursion logic using a stack
def traverse_iterative_part1(row, column, direction):
    stack = [(row, column, direction)]  # Use a stack to simulate recursion

    while stack:
        current_row, current_column, current_direction = stack.pop()

        visited_cells.add((current_row, current_column))

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


# Loop can be identified by identifying whether the same cell is being visited again with the same direction
# Which means it will again go through the same path which means a loop
def traverse_iterative_part2(row, column, direction):
    stack = [(row, column, direction)]  # Use a stack to simulate recursion
    visited = set()
    visited_list = []
    while stack:
        current_row, current_column, current_direction = stack.pop()

        if 0 <= current_row < rows_length and 0 <= current_column < columns_length:
            if (grid[current_row][current_column] == "."):
                if ((current_row, current_column, current_direction) in visited):
                    return True
                else:
                    visited.add((current_row, current_column, current_direction))
                    visited_list.append((current_row, current_column, current_direction))

        next_row = current_row + current_direction[0]
        next_column = current_column + current_direction[1]

        if 0 <= next_row < rows_length and 0 <= next_column < columns_length:
            next_cell = grid[next_row][next_column]

            if next_cell == ".":
                # Move forward in the same direction
                stack.append((next_row, next_column, current_direction))
            elif next_cell == "#":
                # Turn right

                while (True):
                    dir_index = DIRECTIONS.index(current_direction)
                    new_dir_index = (dir_index + 1) % 4
                    new_direction = DIRECTIONS[new_dir_index]

                    new_row = current_row + new_direction[0]
                    new_column = current_column + new_direction[1]

                    # Here there could are position where the right turn leads to another obstacle
                    # At that time, again calculate the direction while in the same cell
                    # Took me a while to find this error since it's a special case
                    if (0 <= new_row < rows_length and 0 <= new_column < columns_length and grid[new_row][
                        new_column] != "."):
                        current_row = current_row
                        current_column = current_column
                        current_direction = new_direction
                    else:
                        break

                if 0 <= new_row < rows_length and 0 <= new_column < columns_length:
                    stack.append((new_row, new_column, new_direction))

    return False


# Execute the traversal
traverse_iterative_part1(row, column, (-1, 0))
print("Cells in path",len(visited_cells))

# Try adding an obstacle to each position in the previous path which guard travelled
# (No need of checking for other cells because it will not impact the guards' path
obstacles = []
for tile in visited_cells:
    grid[tile[0]][tile[1]] = "#"
    is_loop = traverse_iterative_part2(row, column, (-1, 0))
    if (is_loop):
        obstacles.append(tile)
    grid[tile[0]][tile[1]] = "."

print("Total obstacles", len(obstacles))
