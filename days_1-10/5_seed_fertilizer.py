import pandas as pd
from tqdm import trange
from tqdm import tqdm
import random

with open('../input/full/5_seed_fertilizer.txt') as f:
    input = f.readlines()

def process_input():
    mappings = []
    df_mapping = pd.DataFrame(columns=['source', 'dest', 'ran'])
    seeds_rge = input[0].strip('\n').split(':')[1].strip().split(' ')
    seeds_rge = [int(s) for s in seeds_rge]
    seeds= []
    for i in trange(0, len(seeds_rge)-1, 2):
        # seeds.append([random.randint(seeds_rge[i], seeds_rge[i]+seeds_rge[i+1]) for j in
        # range(seeds_rge[i], seeds_rge[i]+seeds_rge[i+1])])
        seeds.append(random.sample(range(seeds_rge[i], seeds_rge[i] + seeds_rge[i + 1]), 1000))

    seeds = [item for sublist in seeds for item in sublist]
    for num, line in enumerate(input[2:]):
        if line == '\n':
            mappings.append(df_mapping.reset_index(drop=True))
            df_mapping = pd.DataFrame(columns=['source', 'dest', 'ran'])
        elif ':' in line:
            pass
        else:
            dest, source, ran = line.strip('\n').split(' ')
            df_mapping_row = pd.DataFrame([[int(source), int(dest), int(ran)]],
                                          columns=['source', 'dest', 'ran'])
            df_mapping = pd.concat([df_mapping, df_mapping_row])
    mappings.append(df_mapping.reset_index(drop=True))

    print(len(seeds))
    return seeds, mappings

def check_seeds(seeds, mapping):
    new_seeds = []
    seeds_replaced = []
    for i, seed in tqdm(enumerate(seeds)):
        for _, row in mapping.iterrows():
            if row['source'] <= seed < row['source']+row['ran']:
                new_seeds.append((seed - row['source']) + row['dest'])
                seeds_replaced.append(i)
        if i not in seeds_replaced:
            new_seeds.append(seed)
    return new_seeds

seeds, mappings = process_input()
for mapping in mappings:
    print(len(seeds))
    seeds = check_seeds(seeds, mapping)

print(min(seeds))