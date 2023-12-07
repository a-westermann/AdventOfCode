import file_ops
from timer import TimeHandler


FiveOfAKind = 6
FourOfAKind = 5
FullHouse = 4
ThreeOfAKind = 3
TwoPair = 2
OnePair = 1
Trash = 0

def get_bucket(hand):
    counts = []
    for card in hand:
        counts.append([card, hand.count(card)])
    counts = convert_js(counts)
    counts = [c[1] for c in counts]
    if 5 in counts:
        return FiveOfAKind
    elif 4 in counts:
        return FourOfAKind
    elif 3 in counts and 2 in counts:
        return FullHouse
    elif 3 in counts:  # or (-1 in hand and 2 in counts):
        return ThreeOfAKind
    elif len([c for c in counts if c == 2]) == 4:
        return TwoPair
    elif 2 in counts:
        return OnePair
    else:
        return Trash

def convert_js(counts) -> (str, int):
    # find the highest count of cards in hand (>1) and convert J
    # ties shouldn't matter
    counts = sorted(counts, key=lambda x: x[1], reverse=True)
    j_count = [c for c in counts if c[0][0] == 'J']
    j_count = 0 if len(j_count) == 0 else j_count[0][1]
    j_applied = False
    for c in counts:
        if c[0] == 'J':
            c[1] = 0 if c[1] < 5 else 5
            continue
        if not j_applied:
            for card in counts:
                card[1] += j_count if card[0] == c[0] else 0
            j_applied = True
    return counts

def get_hand_values(hand):
    return [card_vals[c] for c in hand]


timer = TimeHandler()
input_lines = file_ops.read_input(7)

# Part 1:
# card_vals = {'A':12, 'K':11, 'Q':10, 'J':9, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0}
# Part 2:
card_vals = {'A':12, 'K':11, 'Q':10, 'J':-1, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0}

hand_types = []
buckets = {Trash:[], OnePair:[], TwoPair:[], ThreeOfAKind:[], FullHouse:[], FourOfAKind:[], FiveOfAKind:[]}
for line in input_lines:
    hand, bet = line.split(' ')
    bucket = get_bucket(hand)
    buckets[bucket].append((hand, bet))

# Sort each bucket based on first card, then second card, etc
for bucket, hands in buckets.items():
    sorted_hands = sorted(hands, key=lambda x: get_hand_values(x[0]))
    buckets[bucket] = sorted_hands

total_winnings = 0
rank = 1
for bucket, hands in buckets.items():
    for hand in hands:
        total_winnings += rank * int(hand[1])
        rank += 1

print(f'total winnings {total_winnings}')
print(timer.fetch_time())  # 0.07 seconds
