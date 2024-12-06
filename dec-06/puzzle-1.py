import sys

sys.setrecursionlimit(900000000)

with open("input.txt") as file:
    lines = file.read().splitlines()

grid = []
for line in lines:
    grid.append(list(line))

print(grid)
rows_length, columns_length = len(grid), len(grid[0])

# directions right = (0,1) , left = (0,-1) , up => (-1,0) , down -> (1,0)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West
row, column, direction = 0, 0, (-1,0)

energized_tiles = set()

for x in range(rows_length):
    for k in range(columns_length):
        if (grid[x][k] == '^'):
            row = x
            column = k
            grid[x][k] = "."
            break

print(row, column)
# Travers the grid
def traverse(row, column, direction):
    global energized_tiles
    # print("x", row, column)
    if 0 <= row < rows_length and 0 <= column < columns_length:
        energized_tiles.add((row, column))
        row_n , column_n = row + direction[0], column + direction[1]

        if 0 <= row_n < rows_length and 0 <= column_n < columns_length:
            n_cell = grid[row_n][column_n]
            print(n_cell, row, column)
            if (n_cell == "."):
                # print("ss",row_n, column_n, direction)
                traverse(row_n, column_n, direction)
            elif (n_cell == "#"):

                dir_index = DIRECTIONS.index(direction)
                new_dir_index = (dir_index + 1) % 4
                new_direction = DIRECTIONS[new_dir_index]

                new_position = (row + new_direction[0], column + new_direction[1])

                print("n",new_position, new_direction)
                traverse(new_position[0], new_position[1] , new_direction)
        else:
            # print("sdfsdfsdf")
            return
    else:
        print("33")


try:
    traverse(row, column, (-1, 0))
except:
    print("sdf")
print(len(energized_tiles))


