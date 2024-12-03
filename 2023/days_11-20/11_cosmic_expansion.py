import numpy as np

with open('../input/example/11_cosmic_expansion.txt') as f:
    input = f.readlines()

arr = np.zeros(shape=(len(input), len(input[0])-1))
gals = []
for i, line in enumerate(input):
    line = line.strip('\n')
    for j, char in enumerate(line):
        if char == '.':
            arr[i, j] = 0
        else:
            gals.append([i, j])
            arr[i, j] = 1

def expand_row(a, i, gls):
    # c = a[:i]
    # d = a[i]
    # b = a[i+1:]
    a_ex = np.concatenate([a[:i], np.column_stack((a[i], a[i])).T, a[i+1:]], axis=0)
    for idx, gal in enumerate(gls):
        if gal[0] > i:
            gls[idx][0] += 1
    return a_ex, gls

def expand_col(a, j, gls):
    a_ex = np.concatenate((a[:, :j], np.column_stack((a[:, j], a[:, j])), a[:, j+1:]), axis=1)
    for idx, gal in enumerate(gls):
        if gal[1] > j:
            gls[idx][1] += 1
    return a_ex, gls


arr_ex = arr.copy()
gals_ex = gals.copy()
for i in range(arr.shape[1]):
    if all(arr[i] == 0):
        # this code is the problem, editing arr_ex whilst iterating through it
        arr_ex, gals_ex = expand_row(arr_ex, i, gals_ex)
for j in range(arr.shape[0]):
    if all(arr[:, j] == 0):
        arr_ex, gals_ex = expand_col(arr_ex, j, gals_ex)

def calculate_distances(gl_a, gl_b):
    return abs(gl_a[0] - gl_b[0]) + abs(gl_a[1] - gl_b[1])

def sum_shortest_paths(gls_ex):
    dis = 0
    count = 0
    for idx, gl_a in enumerate(gls_ex):
        for gl_b in gls_ex[idx+1:]:
            count += 1
            dis += calculate_distances(gl_a, gl_b)
    print(count)
    return dis

print(sum_shortest_paths(gls_ex=gals_ex))