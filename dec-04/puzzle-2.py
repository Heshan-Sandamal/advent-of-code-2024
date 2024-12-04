file = open("input.txt")
lines = file.read().splitlines()

matrix = []
for line in lines:
    matrix.append(list(line))

max_row_size = len(matrix[0])
max_height = len(matrix)
print(matrix)


# For X, there could be 4 different ways it could appear
# Index could have value M, and the X would be MAS ↘ with SAM or MAS ↗
# M.S   M.M
# .A.   .A.
# M.S   S.S

# Index could have value S, and the X would be SAM ↘ with SAM or MAS ↗
# S.S   S.M
# .A.   .A.
# M.M   S.M
def is_xmas(x, y):
    tot = 0
    if (matrix[x][y] == "M" and y < max_row_size - 2 and x < max_height - 2 and matrix[x + 1][y + 1] == "A" and
            matrix[x + 2][y + 2] == "S"):
        x2 = x + 2
        if (matrix[x2][y] == "M" and matrix[x2 - 1][y + 1] == "A" and matrix[x2 - 2][y + 2] == "S"):
            tot += 1

        if (matrix[x2][y] == "S" and matrix[x2 - 1][y + 1] == "A" and matrix[x2 - 2][y + 2] == "M"):
            tot += 1

    if (matrix[x][y] == "S" and y < max_row_size - 2 and x < max_height - 2 and matrix[x + 1][y + 1] == "A" and
            matrix[x + 2][y + 2] == "M"):
        x2 = x + 2
        if (matrix[x2][y] == "M" and matrix[x2 - 1][y + 1] == "A" and matrix[x2 - 2][y + 2] == "S"):
            tot += 1
        if (matrix[x2][y] == "S" and matrix[x2 - 1][y + 1] == "A" and matrix[x2 - 2][y + 2] == "M"):
            tot += 1
    return tot


total = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        total += is_xmas(x, y)

print(total)
