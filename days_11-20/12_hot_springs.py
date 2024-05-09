with open('../input/example/12_hot_springs.txt') as f:
    input = f.readlines()

def process_input(line_input):
    spr, grp_size = line_input.strip('\n').split(' ', maxsplit=2)
    grp_sizes = [int(i) for i in grp_size.split(',')]
    return spr, grp_sizes

def gen_init_setup(spr, grp_sizes):
    min_len = sum(grp_sizes) + len(grp_sizes) - 1
    spr_len = len(spr)
    init_setup = []
    for num, i in grp_sizes:
        if num == 0:
            init_setup.append((0, i+1))
        else:
            init_setup.append((grp_sizes[num-1], i+1))


def gen_combin(setup, pos_move):
    pos, str_len = setup[pos_move]
    setup[pos_move] = (pos+1, str_len)
    if pos_move > 0:
        gen_combin(setup, pos_move-1)
    else:
        gen_combin(setup, len(setup))


def find_unique_string_arrangements(lengths, total_length, current_position=0, current_arrangement=[]):
    # Base case: if the lengths list is empty, check if the remaining length is 0
    if current_position == len(lengths):
        return [current_arrangement] if sum(current_arrangement) == total_length else []

    # Recursive case: try placing the current string and move to the next position
    current_length = lengths[current_position]
    arrangements = []

    # Case 1: Add the current string and move to the next position
    if sum(current_arrangement) + current_length <= total_length:
        new_arrangement = current_arrangement + [current_length]
        remaining_arrangements = find_unique_string_arrangements(
            lengths, total_length, current_position + 1, new_arrangement
        )
        arrangements.extend(remaining_arrangements)

    # Case 2: Move to the next position without adding the current string
    remaining_arrangements = find_unique_string_arrangements(
        lengths, total_length, current_position + 1, current_arrangement
    )
    arrangements.extend(remaining_arrangements)

    return arrangements

# Example usage:
lengths = [3, 2, 1]
total_length = 1
unique_arrangements = set(tuple(arrangement) for arrangement in find_unique_string_arrangements(lengths, total_length))
result = list(unique_arrangements)
print(result)
print(f"There are {len(result)} different ways to arrange the strings.")

# spr, grp_sizes = process_input()

