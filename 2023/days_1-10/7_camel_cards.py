def read_input():
    with open('../input/example/7_camel_cards.txt') as f:
        input = f.readlines()

    hands_to_bids = {}
    for line_input in input:
        hand, bid = line_input.strip('\n').split(' ', maxsplit=2)
        hands_to_bids[hand] = bid
    return hands_to_bids

card_deck_to_num = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10
}
card_deck = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
play_list = ['five_oak', 'four_oak', 'full_house', 'three_oak', 'two_pair', 'one_pair', 'high_card']

def categorise_hand(hand):
    char_occ = {}
    contains_joker = False
    for char in hand:
        char_occ[char] = hand.count(char)
        if char == 'J':
            contains_joker = True

    char_occ_sorted = sorted(char_occ, key=char_occ.get, reverse=True)

    if contains_joker:
        for char in char_occ_sorted:
            if char != 'J':
                # highest_char = next(iter(char_occ_sorted))
                char_occ[char] += char_occ['J']
                del char_occ['J']
                hand = hand.replace('J', char)
                break

    char_occ_sorted = sorted(char_occ, key=char_occ.get, reverse=True)

    # doesn't work for ties or
    for char in char_occ_sorted:
        oak = char_occ[char]
        if oak == 5:
            return 'five_oak'
        elif oak == 4:
            return 'four_oak'
        elif oak == 3:
            pair = hand.replace(char, '')
            if pair[0] == pair[1]:
                return 'full_house'
            else:
                return 'three_oak'
        elif oak == 2:
            trip = hand.replace(char, '')
            for c in char_occ_sorted:
                oak_sub = trip.count(c)
                if oak_sub == 2:
                    return 'two_pair'
            return 'one_pair'
    return 'high_card'

def poker_key(hand):
    hand_num = []
    for card in hand:
        if card.isnumeric():
            hand_num.append(int(card))
        else:
            hand_num.append(card_deck_to_num[card])
    return hand_num


def sort_cat(hands_cat):
    return sorted(hands_cat, key=poker_key, reverse=True)


def rank_cards(hands_to_cat):
    sorted_hands = []
    for play in play_list:
        hands_cat = [h for h, c in hands_to_cat.items() if c == play]
        sorted_hands.append(sort_cat(hands_cat))

    hands_to_rank = {}
    for i, hand in enumerate(sum(sorted_hands, [])[::-1]):
        hands_to_rank[hand] = i+1

    return hands_to_rank

hands_to_cat = {}
for hand in read_input():
    hands_to_cat[hand] = categorise_hand(hand)

hand_to_rank = rank_cards(hands_to_cat)
hands_to_bids = read_input()
total = 0
for hand in hand_to_rank:
    total += hand_to_rank[hand] * int(hands_to_bids[hand])

print(total)




