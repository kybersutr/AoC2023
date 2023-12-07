from functools import total_ordering

with open("input.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines() if len(line) > 0]

types = ['HC', '1P', '2P', '3K', 'FH', '4K', '5K']

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

joker_cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


@total_ordering
class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.type = self.get_type()

    def __hash__(self):
        return hash(repr(self))

    def get_type(self):
        if len(set(self.cards)) == 1:
            return '5K'
        elif len(set(self.cards)) == 2:
            if self.cards.count(self.cards[0]) == 4 or self.cards.count(self.cards[1]) == 4:
                return '4K'
            else:
                return 'FH'
        elif len(set(self.cards)) == 3:
            if self.cards.count(self.cards[0]) == 3 \
                    or self.cards.count(self.cards[1]) == 3 \
                    or self.cards.count(self.cards[2]) == 3:
                return '3K'
            else:
                return '2P'
        elif len(set(self.cards)) == 4:
            return '1P'
        else:
            return 'HC'

    def __repr__(self):
        return self.cards

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if types.index(self.type) < types.index(other.type):
            return True
        elif types.index(self.type) > types.index(other.type):
            return False
        else:
            self_num = list(map(lambda x: cards.index(x), self.cards))
            other_num = list(map(lambda x: cards.index(x), other.cards))
            return self_num < other_num

@total_ordering
class JokerHand:

    def __init__(self, cards):
        self.cards = cards
        self.type = self.get_type()

    def __hash__(self):
        return hash(repr(self))

    def get_type(self):
        if len(set(self.cards)) == 1 or (len(set(self.cards)) == 2 and 'J' in self.cards):
            return '5K'
        elif len(set(self.cards)) == 2 or (len(set(self.cards)) == 3 and 'J' in self.cards):
            if self.cards.count('J') == 3:
                return '4K'
            elif self.cards.count('J') == 2:
                return '4K'
            elif self.cards.count('J') == 1 and \
                    (self.cards.count(self.cards[0]) == 3 or
                     self.cards.count(self.cards[1]) == 3 or
                     self.cards.count(self.cards[2]) == 3):
                return '4K'
            elif self.cards.count(self.cards[0]) == 4 or self.cards.count(self.cards[1]) == 4:
                return '4K'
            else:
                return 'FH'
        elif len(set(self.cards)) == 3 or (len(set(self.cards))) == 4 and 'J' in self.cards:
            if 'J' not in self.cards:
                if self.cards.count(self.cards[0]) == 3 \
                    or self.cards.count(self.cards[1]) == 3 \
                    or self.cards.count(self.cards[2]) == 3:
                        return '3K'
                return '2P'
            else:
                return '3K'
        elif len(set(self.cards)) == 4 or self.cards.count('J') == 1:
            return '1P'
        else:
            return 'HC'

    def __repr__(self):
        return self.cards

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if types.index(self.type) < types.index(other.type):
            return True
        elif types.index(self.type) > types.index(other.type):
            return False
        else:
            self_num = list(map(lambda x: joker_cards.index(x), self.cards))
            other_num = list(map(lambda x: joker_cards.index(x), other.cards))
            return self_num < other_num

def first():
    hands_and_values = {}

    for line in lines:
        parts = line.split()
        hand = Hand(parts[0])
        value = int(parts[1])
        hands_and_values[hand] = value

    compared_hands = sorted(hands_and_values.keys())
    total = 0
    for i in range(len(compared_hands)):
        total += (i+1) * hands_and_values[compared_hands[i]]

    return total

def second():
    hands_and_values = {}

    for line in lines:
        parts = line.split()
        hand = JokerHand(parts[0])
        value = int(parts[1])
        hands_and_values[hand] = value

    compared_hands = sorted(hands_and_values.keys())
    total = 0
    for i in range(len(compared_hands)):
        total += (i+1) * hands_and_values[compared_hands[i]]

    return total

print(first())
print(second())

fives = ['AAAAA', 'AAAAJ', 'JAAAJ', 'AJAJJ', 'JAJJJ', 'JJJJJ']
fours = ['AABAA', 'AJBAA', 'JABJA', 'JJBAJ']
full_houses = ['AABAB', 'AJBAB']
threes = ['AABAC', 'CABAJ', 'CABJJ']