with open("input.txt") as file:
    lines = file.read().splitlines()

grid = []
for line in lines:
    grid.append(list(line))

rows_length, columns_length = len(grid), len(grid[0])

# directions right = (0,1) , left = (0,-1) , up => (-1,0) , down -> (1,0)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West
row, column, direction = 0, 0, (-1, 0)

for x in range(rows_length):
    for k in range(columns_length):
        if (grid[x][k] == '^'):
            row = x
            column = k
            grid[x][k] = "."
            break

visited_cells = set()


# Travers the grid
# I think this should give the answer, but it exceeds the recursion limit.
# Hence, had to change recursion to a loop
def traverse(row, column, direction):
    global visited_cells
    if 0 <= row < rows_length and 0 <= column < columns_length:
        visited_cells.add((row, column))
        row_n, column_n = row + direction[0], column + direction[1]

        if 0 <= row_n < rows_length and 0 <= column_n < columns_length:
            n_cell = grid[row_n][column_n]
            if (n_cell == "."):
                traverse(row_n, column_n, direction)
            elif (n_cell == "#"):

                dir_index = DIRECTIONS.index(direction)
                new_dir_index = (dir_index + 1) % 4
                new_direction = DIRECTIONS[new_dir_index]

                new_position = (row + new_direction[0], column + new_direction[1])

                print("n", new_position, new_direction)
                traverse(new_position[0], new_position[1], new_direction)
        else:
            return
    else:
        print("33")


traverse(row, column, (-1, 0))
print(len(visited_cells))
