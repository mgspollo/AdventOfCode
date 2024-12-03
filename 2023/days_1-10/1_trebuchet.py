import math
import string

with open('../input/full/1_trebuchet.txt') as f:
    input = f.readlines()

def remove_letters(input_string):
    numbers = {
        'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
    }
    sub_string, rsub_string = '', ''
    input_string = input_string.strip('\n')
    for fletter, lletter in zip(input_string, input_string[::-1]):
        sub_string = sub_string + fletter
        rsub_string = lletter + rsub_string
        for num in numbers:
            try:
                sub_string.index(num)
                sub_string = sub_string.replace(num, str(numbers[num]))
            except ValueError:
                pass
            try:
                rsub_string.index(num)
                rsub_string = rsub_string.replace(num, str(numbers[num]))
            except ValueError:
                pass
    sub_string = sub_string.strip(string.ascii_lowercase)
    rsub_string = rsub_string.strip(string.ascii_lowercase)
    return [sub_string[0], rsub_string[-1]]


sum_total = 0
for line in input:
    digits = remove_letters(line)
    sum_total += int(digits[0] + digits[1])

print(sum_total)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
