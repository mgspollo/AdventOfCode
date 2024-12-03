with open('../input/example/13_mirrors.txt') as f:
    input = f.readlines()

def process_input(line_input):
    spr, grp_size = line_input.strip('\n').split(' ', maxsplit=2)
    grp_sizes = [int(i) for i in grp_size.split(',')]
    return spr, grp_sizes