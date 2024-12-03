with open('../input/2_red_nosed_reports.txt') as f:
    input = f.readlines()

def unsafe_decreasing_level_with_remove(chars):
    for i in range(len(chars)):
        chars_removed = [element for num, element in enumerate(chars) if num != i]
        if not unsafe_decreasing_level(chars_removed):
            return False
    return True

def unsafe_increasing_level_with_remove(chars):
    for i in range(len(chars)):
        chars_removed = [element for num, element in enumerate(chars) if num != i]
        if not unsafe_increasing_level(chars_removed):
            return False
    return True

def unsafe_decreasing_level(chars):
    for i in range(len(chars) - 1):
        if (chars[i + 1] - chars[i] >= 0) or (chars[i + 1] - chars[i] < -3):
            return True

def unsafe_increasing_level(chars):
    for i in range(len(chars) - 1):
        if (chars[i] - chars[i + 1] >= 0) or (chars[i + 1] - chars[i] > 3):
            return True

unsafe = 0
for line in input:
    chars = line.strip('\n').split(' ')
    chars = [int(char) for char in chars]
    if chars[0] > chars[-1]:
        if unsafe_decreasing_level(chars):
            if unsafe_decreasing_level_with_remove(chars):
                unsafe += 1
    elif chars[-1] > chars[0]:
        if unsafe_increasing_level(chars):
            if unsafe_increasing_level_with_remove(chars):
                unsafe += 1
    else:
        unsafe += 1

print(unsafe)
print(len(input) - unsafe)


