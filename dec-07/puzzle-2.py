import itertools

file = open("input.txt")
lines = file.read().splitlines()

# Keep total and numbers array
total_array, numbers_array = [], []
for line in lines:
    data = line.split(":")
    total, numbers = int(data[0]), data[1].strip().split(" ")
    total_array.append(total)
    numbers_array.append(numbers)

total_result = 0
for i in range(len(total_array)):
    # Get different permutations of each operator for size (length_of_number - 1) since operator are 1 less than numbers
    all_permutations = list(itertools.product(['+', '*', "||"], repeat=len(numbers_array[i]) - 1))
    for perm in all_permutations:
        total = 0
        equation = numbers_array[i][0]
        for h in range(1, len(numbers_array[i])):
            if (perm[h - 1] == "||"):
                equation = equation + numbers_array[i][h]  # If || is the operator, then concatenate
            else:
                equation = equation + perm[h - 1] + numbers_array[i][h]
            total = eval(equation)
            equation = str(total)  # Replace equation with calculated value (Since calculation happens from left->Right)

            # if total > expected value, break since total already exceeds the expected value
            if (total > total_array[i]):
                break

        if (total == total_array[i]):
            total_result += total
            break

print(total_result)
