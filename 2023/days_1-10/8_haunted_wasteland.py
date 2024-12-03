from ast import literal_eval as make_tuple
import math

with open('../input/full/8_haunted_wasteland.txt') as f:
    input = f.readlines()

lr_inst = input[0].strip('\n')

s_to_f = {}
for line in input[2:]:
    node_s, node_f = line.strip('\n').split(' = ')
    node_f = tuple(map(str, node_f.replace('(','').replace(')','').split(', ')))
    s_to_f[node_s] = node_f


start_nodes = []
for node in s_to_f:
    if node[-1] == 'A':
        start_nodes.append(node)


def lcm(node_to_counter):
    prev_counter = 1
    for node in node_to_counter:
        lcm = math.lcm(node_to_counter[node], prev_counter)
        prev_counter = node_to_counter[node]
    return lcm


# node = 'AAA'
node_to_counter = {}
for node in start_nodes:
    i = 0
    counter = 0
    while node[-1] != 'Z':
        counter += 1
        node_f = s_to_f[node]
        if lr_inst[i] == 'L':
            node = node_f[0]
        elif lr_inst[i] == 'R':
            node = node_f[1]
        if i < len(lr_inst)-1:
            i += 1
        else:
            i = 0
    node_to_counter[node] = counter

print(lcm(node_to_counter))

