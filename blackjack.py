import random as rd

cards = {
    chr(0x1F0A1): 11,
    chr(0x1F0A2): 2,
    chr(0x1F0A3): 3,
    chr(0x1F0A4): 4,
    chr(0x1F0A5): 5,
    chr(0x1F0A6): 6,
    chr(0x1F0A7): 7,
    chr(0x1F0A8): 8,
    chr(0x1F0A9): 9,
    chr(0x1F0AA): 10,
    chr(0x1F0AB): 10,
    chr(0x1F0AD): 10,
    chr(0x1F0AE): 10,
}


def create_deck():
    _deck = []
    i = 0
    for card, value in cards.items():
        _deck.append((card, "hearts", value))
        _deck.append((card, "spades", value))
        _deck.append((card, "club", value))
        _deck.append((card, "diamonds", value))

    # Randomize the deck
    _random_deck = []
    for i in range(len(_deck)):
        card_index = rd.randint(
            0, len(_deck) - 1
        )  # Need to subtract 1 because of list indexing
        _random_deck.append(_deck.pop(card_index))
    return _random_deck


deck = create_deck()
print(deck)  # TODO: Remove after tests


class Player:
    def __init__(self, money):
        self.money = float(money)

    hand = []  # Cards in the hand

    def get_hand_value(self):
        points = 0
        for card in self.hand:
            points += card[2]
        return points

