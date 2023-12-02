with open('input/day2.txt') as f:
    input = f.readlines()

GAME_CONFIG = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def subgame_is_possible(subgame_dict):
    for colour in GAME_CONFIG:
        if subgame_dict[colour] > GAME_CONFIG[colour]:
            return False
    return True


def get_game_values(line_input):
    game_num, game_input = line_input.strip('\n').split(':', maxsplit=2)
    game_num = game_num.split(' ', maxsplit=1)[1]
    game_inputs = [i.strip() for i in game_input.split(';')]
    game_list = []
    for game in game_inputs:
        coloured_balls = [i.strip() for i in game.split(',')]
        subgame_dict = {
            'blue': 0,
            'green': 0,
            'red': 0
        }
        for j in coloured_balls:
            num_balls, colour_balls = j.split(' ', maxsplit=1)
            subgame_dict[colour_balls] = int(num_balls)
        game_list.append(subgame_dict)
    return game_num, game_list


def minimum_cubes_required(game_list):
    col_min = {
        'blue': 0,
        'green': 0,
        'red': 0
    }
    for subgame_dict in game_list:
        for colour in GAME_CONFIG:
            col_min[colour] = max(col_min[colour], subgame_dict[colour])
    return col_min

def power_of_game(col_min):
    power = 1
    for _, min_num in col_min.items():
        power *= min_num
    return power


def game_is_possible(game_list):
    for num, subgame_dict in enumerate(game_list):
        game_list[num] = subgame_is_possible(subgame_dict)
    return all(game_list)


def count_game_scores_p2(cum_game_scores, line_input):
    game_num, game_list = get_game_values(line_input)
    cum_game_scores += power_of_game(minimum_cubes_required(game_list))
    return cum_game_scores

def count_game_scores(cum_game_num, line_input):
    game_num, game_list = get_game_values(line_input)
    if game_is_possible(game_list):
        cum_game_num += int(game_num)
        return cum_game_num
    else:
        return cum_game_num

# part 1
cum_game_num = 0
cum_game_scores = 0
for line in input:
    cum_game_num = count_game_scores(cum_game_num, line)
    cum_game_scores = count_game_scores_p2(cum_game_scores, line)

print (cum_game_num)
print(cum_game_scores)

# part 2