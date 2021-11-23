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

    print("Shuffling the deck ", end="")
    for i in range(3):
        sleep(1.5)
        print(".", end="")
    print()
    sleep(2.5)

    # Randomize the deck
    _random_deck = []
    for i in range(len(_deck)):
        card_index = rd.randint(
            0, len(_deck) - 1
        )  # Need to subtract 1 because of list indexing
        _random_deck.append(_deck.pop(card_index))

    print("Deck shuffled")
    sleep(2)
    return _random_deck



# Obtener valor de carta
def card_value(_card):
    return _card[0][2]

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
            return self.new_card[0]

    def empty_hand(self):
        self.hand = []

    def print_hand(self, player, is_self=False):
        player_hand = []
        for card in player.hand:
            if is_self == True:
                player_hand.append(card[0])
            elif card[1] == "covered":
                player_hand.append("covered card")
            else:
                player_hand.append(card[0])

        return player_hand


class Visitor(Player):
    def play_hand(self):
        print("It's your turn.")
        sleep(2)
        print("Your hand is")
        print(self.print_hand(self))
        sleep(2)

        self.state = "playing"
        option_help = True
        while self.state == "playing":
            if option_help == True:
                option_help = False
                print("Choose your action between:")
                sleep(1.5)
                print("hit: take another card.")
                sleep(1.5)
                print("see my hand: see a list of the cards in your hand.")
                sleep(1.5)
                print("see dealer hand: see uncovered dealer's card.")
                sleep(1.5)
                print("stand: pass the game to the dealer.")
                sleep(1.5)
                option = input("What do you choose? ").casefold()
            else:
                option = input("Choose your option: ")

            if option == "hit":
                print("You get a card")
                sleep(1)
                print(self.get_card(see_card=True))
                sleep(2)
                print("Your hand is now")
                print(self.print_hand(self))

            elif option == "stand":
                self.state = "standing"
                print("You are now standing with {} points".format(self.get_hand_value()))

            elif option == "see my hand":
                print("Your hand is")
                print(self.print_hand(self))

            elif option == "see dealer hand":
                print("The dealer's hand is")
                print(self.print_hand(dealer))

            elif option == "help":
                option_help = True
                continue

            else:
                print("The dealer didn't understand you.")
                sleep(2)
                print('(Type "help" to see again the list of commands)')

            sleep(2)


            if self.get_hand_value() > 21:
                self.state = "busted"
                print("You went bust (over 21)")

            elif self.get_hand_value() == 21:
                self.state = "standing"
                print("You got 21! You stand with maximum points")

            sleep(3)


class Dealer(Player):  # Dealer will play automatically depending on its hand
    def play_hand(self):
        print("It is the dealer's turn.")
        sleep(2)
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

deck = []
dealer = Dealer(0)
p1 = Visitor(0)

### Plays a whole round
def play_round():

    p1.empty_hand()
    dealer.empty_hand()

    p1.get_card()
    p1.get_card()
    dealer.get_card()
    dealer.get_card(covered=True)

    p1.play_hand()
    if p1.state == "standing":
        dealer.play_hand()



### Actual game
playing = True
while playing:
    deck = create_deck()
    play_round()

    if p1.state == "busted":
        print("You lost your bet. Want to try again?")
    elif p1.state == "standing" and dealer.state == "standing":
        if p1.get_hand_value() > dealer.get_hand_value():
            print("You won the hand! Want to play another one?")
        else:  # Your score is under the dealer one or equal
            print("Your score didn't surpass the dealer's one. Want to try again?")
    else:  # dealer.state == "busted"
        print("You won the hand! Want to play another one?")

    sleep(2)

    while True:
        want_to_play = input('(Type "yes" to play another round, or "no" to stop playing): ')
        if want_to_play == "yes":
            break
        elif want_to_play == "no":
            sleep("See you soon!")
            sleep(2)
            playing = False
            break
        else:
            print("Please select one of the options\r")
            sleep(3)
