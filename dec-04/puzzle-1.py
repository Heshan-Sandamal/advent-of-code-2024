file = open("input.txt")
lines = file.read().splitlines()

matrix = []
for line in lines:
    matrix.append(list(line))

max_row_size = len(matrix[0])
max_height = len(matrix)
print(matrix)


# XMAS value can appear is 8 different ways per index when it starts from X
# ↖ ↑ ↗
# ← · →
# ↙ ↓ ↘
def is_xmas(x, y):
    tot = 0
    if (y < max_row_size - 3 and matrix[x][y + 1] == "M" and matrix[x][y + 2] == "A" and matrix[x][y + 3] == "S"):
        tot += 1  # →
    if (y > 2 and matrix[x][y - 1] == "M" and matrix[x][y - 2] == "A" and matrix[x][y - 3] == "S"):
        tot += 1 # ←
    if (x < max_height - 3 and matrix[x + 1][y] == "M" and matrix[x + 2][y] == "A" and matrix[x + 3][y] == "S"):
        tot += 1 # ↓
    if (x > 2 and matrix[x - 1][y] == "M" and matrix[x - 2][y] == "A" and matrix[x - 3][y] == "S"):
        tot += 1 # ↑
    if (y < max_row_size - 3 and x < max_height - 3 and matrix[x + 1][y + 1] == "M" and matrix[x + 2][y + 2] == "A" and
            matrix[x + 3][y + 3] == "S"):
        tot += 1 # ↘
    if (y > 2 and x > 2 and matrix[x - 1][y - 1] == "M" and matrix[x - 2][y - 2] == "A" and matrix[x - 3][
        y - 3] == "S"):
        tot += 1 # ↖
    if (x < max_height - 3 and y > 2 and matrix[x + 1][y - 1] == "M" and matrix[x + 2][y - 2] == "A" and matrix[x + 3][
        y - 3] == "S"):
        tot += 1 # ↙
    if (x > 2 and y < max_row_size - 3 and matrix[x - 1][y + 1] == "M" and matrix[x - 2][y + 2] == "A" and
            matrix[x - 3][y + 3] == "S"):
        tot += 1 # ↗

    return tot


total = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if (matrix[x][y] == "X"):
            # When index has the value X, then XMAS could appear in 8 different ways
            total += is_xmas(x, y)

print(total)
