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

def create_deck(length=1):  # Length represents the number of individual decks that form the big deck.
    _deck = []
    for i in range(length):
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

# Obtener valor de carta
def card_value(_card):
    return _card[0][2]

deck = None

class Player:
    def __init__(self, money):
        self.money = float(money)
        self.hand = []  # Cards in the hand
        self.state = "waiting"

    hand = []  # Cards in the hand

    def get_hand_value(self):
        points = 0
        for card in self.hand:
            points += card_value(card)
        return points

    def get_card(self, see_card=False, covered=False):
        self.new_card = deck.pop()
        if covered == True:
            self.new_card = (self.new_card, "covered")
        else:
            self.new_card = (self.new_card, "uncovered")

        self.hand.append(
            self.new_card
        )
        if see_card == True:
            return self.new_card

    def empty_hand(self):
        self.hand = []


class Visitor(Player):
    def play_hand(self):
        self.state = "playing"
        while self.state == "playing":
            option = input('Choose your action (type "help" for a list of actions): ').casefold()  # TODO: El parentesis va a ser muy repetitivo. Planear un tutorial al inicio con las acciones disponibles. Usar \r para reescribir

            if option == "hit":
                print("You get a card")
                sleep(1)
                print(self.get_card(see_card=True))
                sleep(2)
                print("Your hand is now")
                print(self.hand)

            elif option == "stand":
                self.state = "standing"
                print()

            elif option == "see my hand":
                print("Your hand is")
                my_hand = []
                for card in self.hand:
                    my_hand.append(card[0])
                print(my_hand)

            elif option == "see dealer hand":
                dealer_hand = []
                for card in dealer.hand:
                    if card[1] == "covered":
                        dealer_hand.append("covered card")
                    else:
                        dealer_hand.append(card[0])
                return dealer_hand

            else:
                print("The dealer didn't understand you.")
                sleep(2)
                print('(Type "help" to get a list of comands)')
            sleep(2)


            if self.get_hand_value() > 21:
                self.state = "busted"
                print("You went bust (over 21) and lost your money. Better luck next time!")
            elif self.get_hand_value() == 21:
                self.state = "standing"
                print("You got 21! You stand with maximum points")


class Dealer(Player):  # Dealer will play automatically depending on its hand
    def play_hand(self):
        self.state = "playing"
        while self.state == "playing":

            self.hand_value = self.get_hand_value()
            print("The dealer has {} points in his hand".format(self.hand_value))
            sleep(2)

            if self.hand_value < 17:
                print("The dealer gets a card")
                self.get_card()

            elif 17 <= self.hand_value <= 21:
                print("The dealer stands with {} points".format(self.hand_value))
                self.state = "standing"

            else:  # hand_value > 21
                print("The dealer went bust")
                self.state = "busted"

            sleep(2)





dealer = Dealer(100000)
p1 = Visitor(2000)


### Start hand
deck = create_deck()

p1.get_card()
p1.get_card()
dealer.get_card()
dealer.get_card(covered=True)

p1.play_hand()
if p1.state == "standing":
    dealer.play_hand()


# You should be able to see only ONE card from the dealer. Add property to card, to be uncovered or covered. Function property