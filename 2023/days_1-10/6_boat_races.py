# with open('input/day6.txt') as f:
#     input = f.readlines()
from tqdm import tqdm

def is_race_cr(time_button, cr_time, cr_dis):
    race_dis = (cr_time - time_button) * time_button
    if cr_dis < race_dis:
        return True
    else:
        return False

def get_race_possibilities(cr_time, cr_dis):
    counter = 0
    for t in tqdm(range(1, cr_time)):
        if is_race_cr(t, cr_time, cr_dis):
            counter += 1
    return counter

mult_pos = 1
for time, dis in zip([48938466], [261119210191063]):
    mult_pos *= get_race_possibilities(time, dis)

print(mult_pos)
