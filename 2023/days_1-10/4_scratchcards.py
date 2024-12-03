with open('../input/full/4_scratchcards.txt') as f:
    input = f.readlines()

def get_card_values(line_input, win_list, num_copies, line_num):
    card_num, card_input = line_input.strip('\n').split(':', maxsplit=2)
    if line_num < 10:
        card_num = int(card_num.split('   ', maxsplit=2)[1])
    elif line_num < 100:
        card_num = int(card_num.split('  ', maxsplit=2)[1])
    else:
        card_num = int(card_num.split(' ', maxsplit=2)[1])
    win_num, scr_num = card_input.split('|', maxsplit=2)

    wins_set = set([int(i.strip()) for i in win_num.strip().split(' ') if i != ''])
    scrs_set = set([int(i.strip()) for i in scr_num.strip().split(' ') if i != ''])

    inter = set.intersection(wins_set, scrs_set)
    exp = len(inter) - 1

    if num_copies > 0:
        if card_num+exp >= len(input)+1:
            upper_lim = len(input)+1
        else:
            upper_lim = card_num+exp+1
        win_list += [i for i in range(card_num+1, upper_lim+1) for _ in range(num_copies)]

    return win_list
    # win_nums = [i.strip() for i in win_num.strip().split(' ')]
    # scr_nums = [i.strip() for i in scr_num.strip().split(' ')]


cum_game_score = 0
win_list = list(range(1, len(input)+1))
for line, w in zip(input, win_list):
    win_list = get_card_values(line, win_list, num_copies=win_list.count(w), line_num=w)

print(len(win_list))