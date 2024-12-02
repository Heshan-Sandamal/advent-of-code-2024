file = open("input.txt")
lines = file.read().splitlines()

# Check the diff condition
def check_diff(a, b):
    return 1 <= abs(a - b) <= 3

# Get Sequence Type
def get_sequence_type(a, b):
    if (b > a):
        return 1  # increment sequence
    else:
        return 2  # decrement sequence


reports = []
for text in lines:
    reports.append([int(x) for x in text.split(" ")])

# Check each report fulfils the given conditions by comparing adjacent elements in each report
# Based on the comparison, identify whether the difference condition is met and type of the list (increment/decrement)
# Check whether those conditions are met by all levels in a report
total = 0
for levels in reports:
    seq_type , is_safe = -1 , True
    for i in range(len(levels) - 1):

        if (check_diff(levels[i], levels[i + 1])):
            seq_type_new = get_sequence_type(levels[i], levels[i + 1])

            if (seq_type != -1 and seq_type != seq_type_new):
                is_safe = False
                break

            seq_type = seq_type_new
        else:
            is_safe = False
            break

    if (is_safe):
        total += 1

print(total)
