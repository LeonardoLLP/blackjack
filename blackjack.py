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

# Obtener valor de carta
def card_value(_card):
    return _card[2]

class Player:
    def __init__(self, money):
        self.money = float(money)

    state = "waiting"

    hand = []  # Cards in the hand

    def get_hand_value(self):
        points = 0
        for card in self.hand:
            points += card_value(card)
        return points

    def get_card(self):
        self.hand.append(
            deck.pop()
        )  # No need to specify deck: always the same. Only one deck

    def empty_hand(self):
        self.hand = []


# TODO: Change location of this
dealer = Player(100000)
p1 = Player(2000)

### Start hand

p1.get_card()
p1.get_card()

dealer.get_card()
dealer.get_card()  # TODO: Esta carta tiene que estar cubierta. El jugador puede ver la primera carta pero no la segunda.

p1.state = "on play"
while p1.state == "on play":
    option = input('Choose your action (type "help" for a list of actions): ')  # TODO: El parentesis va a ser muy repetitivo. Planear un tutorial al inicio con las acciones disponibles. Usar \r para reescribir

    if option == "hit":
        pass
    if option == "see my hand":
        pass
    if option == "stand":
        pass

    if p1.get_hand_value > 21:
        p1.state = "busted"
    elif p1.get_hand_value == 21:
        p1.state = "standing"

