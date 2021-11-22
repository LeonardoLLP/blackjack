import random as rd
from time import sleep

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
        self.hand = []  # Cards in the hand

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
dealer.get_card()  # Every card can be uncovered

print()
print(dealer.hand)
print(p1.hand)  # TODO: remove after tests

p1.state = "on play"
while p1.state == "on play":
    option = input('Choose your action (type "help" for a list of actions): ')  # TODO: El parentesis va a ser muy repetitivo. Planear un tutorial al inicio con las acciones disponibles. Usar \r para reescribir

    if option == "hit":
        pass
    elif option == "see my hand":
        pass
    elif option == "stand":
        p1.state = "standing"
    else:
        print("The dealer didn't understand you.")
        sleep(0.75)
        print('(Type "help" to get a list of comands)')
        sleep(0.75)

    if p1.get_hand_value() > 21:
        p1.state = "busted"
    elif p1.get_hand_value() == 21:
        p1.state = "standing"

