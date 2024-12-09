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


# Calculate all anti-nodes per each pair locates in same line
def calculate_distance(elem1, elem2):
    antinodes = set()

    x_dis = elem2[0] - elem1[0]
    y_dis = elem2[1] - elem1[1]

    # Calculate all anti-nodes from antenna 1 including antenna 1
    antinodes.add(elem1)
    while (True):
        ant_1 = (elem1[0] - x_dis, elem1[1] - y_dis)
        if (inside_matrix((ant_1[0], ant_1[1]))):
            antinodes.add(ant_1)
            elem1 = ant_1
        else:
            break

    # Calculate all anti-nodes from antenna 2 including antenna 2
    antinodes.add(elem2)
    while (True):
        ant_2 = (elem2[0] + x_dis, elem2[1] + y_dis)

        if (inside_matrix((ant_2[0], ant_2[1]))):
            antinodes.add(ant_2)
            elem2 = ant_2
        else:
            break

    return antinodes


# Check whether anti-node location is inside the grid
def inside_matrix(dt):
    return 0 <= dt[0] < rows_length and 0 <= dt[1] < columns_length


all_antinodes = set()
for l in locations:
    elements = locations.get(l)

    pairs = itertools.combinations(elements, 2)  # Get all distinct pairs of antennas for each antenna type

    for pair in list(pairs):
        all_nodes = calculate_distance(pair[0], pair[1])
        all_antinodes.update(all_nodes)

print(len(all_antinodes))
