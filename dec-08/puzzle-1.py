import itertools

file = open("input.txt")
lines = file.read().splitlines()

grid = []
for line in lines:
    grid.append(list(line))

rows_length, columns_length = len(grid), len(grid[0])

# Get locations per each antenna type
locations = {}
for x in range(rows_length):
    for y in range(columns_length):
        if (grid[x][y] != '.'):
            if (grid[x][y] not in locations):
                locations[grid[x][y]] = [(x, y)]
            else:
                locations[grid[x][y]].append((x, y))


# Calculate the anti-node distance
# Calculate the x and y distance between each pair of antennas
# Then locate anti-nodes based on that.
# Anti-node 1 -> 2 * distance from Antenna 2 same as ( Antenna1_location - distance )
# Anti-node 2 -> 2 * distance from Antenna 1 same as ( Antenna2_location + distance )
def calculate_distance(elem1, elem2):
    x_dis = elem2[0] - elem1[0]
    y_dis = elem2[1] - elem1[1]

    ant_1 = (elem1[0] - x_dis, elem1[1] - y_dis)  # Antenna 1 location - distance
    ant_2 = (elem2[0] + x_dis, elem2[1] + y_dis)  # Antenna 2 location + distance

    return ant_1, ant_2


# Check whether anti-node location is inside the grid
def inside_matrix(node):
    return 0 <= node[0] < rows_length and 0 <= node[1] < columns_length


all_antinodes = set()
for l in locations:
    elements = locations.get(l)
    pairs = itertools.combinations(elements, 2)  # Get all distinct pairs of antennas for each antenna type

    for pair in list(pairs):
        ant_1, ant_2 = calculate_distance(pair[0], pair[1])

        if (inside_matrix((ant_1[0], ant_1[1]))):
            all_antinodes.add(ant_1)

        if (inside_matrix((ant_2[0], ant_2[1]))):
            all_antinodes.add(ant_2)

print(len(all_antinodes))
