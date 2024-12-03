with open('../input/3_mull_it_over.txt') as f:
    input = f.readlines()

import re

chars = str()
for line in input:
    chars = chars + line.strip('\n')

do_or_dont = re.findall(r"do\(\)|don't\(\)", chars)
split_chars = re.split(r"do\(\)|don't\(\)", chars)

mul = 0
for i, segment in enumerate(split_chars):
    if i == 0:
        x = re.findall(r"\bmul\(\b\d+,\d+\)", segment)
        for match in x:
            nums = re.findall(r"\d+", match)
            mul += int(nums[0]) * int(nums[1])
    elif do_or_dont[i-1] == 'don\'t()':
        pass
    else:
        x = re.findall(r"\bmul\(\b\d+,\d+\)", segment)
        for match in x:
            nums = re.findall(r"\d+", match)
            mul += int(nums[0]) * int(nums[1])

print(mul)