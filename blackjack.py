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
    return _deck

deck = create_deck()
print(deck)