import numpy as np
import pandas as pd
import string

with open('../input/full/3_gear_ratios.txt') as f:
    lines = f.readlines()
    input_lines = []
    for line in lines:
        input_lines.append([str(i) for i in line.strip('\n')])

def check_adjacent_cells(row, start_col, end_col):
    symbol_list = ['!', '£', '$', '%', '^', '&', '*', '@', '#', '+', '/', '-', '=']
    for i_a in range(row - 1, row + 2):
        for j_a in range(start_col - 1, end_col + 1):
            cell = a_pad[i_a, j_a]
            if any(cell == x for x in symbol_list):
                return True
    return False

def check_adjacent_cells_gears(row, start_col, end_col):
    symbol_list = ['*']
    for i_a in range(row - 1, row + 2):
        for j_a in range(start_col - 1, end_col + 1):
            cell = a_pad[i_a, j_a]
            if any(cell == x for x in symbol_list):
                cell_coord = (i_a, j_a)
                return cell_coord
    return False


a = np.column_stack(input_lines).T
row_num, col_num = a.shape
a_pad = np.pad(a, 1, mode='constant', constant_values='.')
# df_digit = pd.DataFrame(columns=['number', 'start', 'end', 'is_valid'])
df_digit = pd.DataFrame(columns=['number', 'start', 'end', 'star_coords'])
for i in range(1, row_num+1):
    digit_num = 0
    for j in range(1, col_num+1):
        if j < digit_num:
            j = digit_num
        if any(a_pad[i, j] == str(x) for x in range(0, 10)):
            digit_num = j
            digit_str = str()
            while any(a_pad[i, digit_num] == str(x) for x in range(0, 10)):
                digit_str += a_pad[i, digit_num]
                digit_num += 1
            df_digit.loc[len(df_digit.index)] = [
                int(digit_str),
                (i, j),
                (i, digit_num),
                check_adjacent_cells_gears(i, j, digit_num)
            ]
            j = digit_num
            # df_digit['number'] = int(digit_str)
            # df_digit['start'] = (i, j)
            # df_digit['end'] = (i, digit_num)
            # df_digit['is_valid'] = check_adjacent_cells(i, j, digit_num)

df_digit_gears = df_digit[df_digit.star_coords]


