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


# Check the given report is safe or not
def check_report(levels, sequence_type):

    for i in range(len(levels) - 1):

        if (check_diff(levels[i], levels[i + 1])):
            sequence_type_new = get_sequence_type(levels[i], levels[i + 1])

            if (sequence_type != -1 and sequence_type != sequence_type_new):
                return False
            sequence_type = sequence_type_new

        else:
            return False
    return True


# Get All levels permutations removing one element from a given report at once
def get_all_perm(levels):
    new_levels_perm = []
    for x in range(len(levels)):
        new_levels_perm.append([levels[y] for y in range(len(levels)) if (x != y)])
    return new_levels_perm


reports = []
for text in lines:
    reports.append([int(x) for x in text.split(" ")])

# I'm using the brute force approach since the lists are short
# Check the conditions are met like in puzzle-1
# If not get all permutations of lists by removing each element at once
# Check above conditions are met of at least one permutation
total = 0
for levels in reports:
    is_safe = check_report(levels, -1)

    if (is_safe):
        total += 1
    else:
        all_level_perms = get_all_perm(levels)

        for new_levels in all_level_perms:
            is_safe = check_report(new_levels, -1)
            if (is_safe):
                total += 1
                break

print(total)
