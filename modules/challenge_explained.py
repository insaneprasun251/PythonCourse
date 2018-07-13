import random

playing = False
chip_pool = 100
bet = 1
restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"

# Hearts, Diamonds, Clubs, Spades
suits = ('H', 'D', 'C', 'S')

# Possible card ranks
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Point values dict (Note: Aces can also be 11, check self.ace for details)
card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Player(object):
    def __init__(self, bankroll=100):
        self.bankroll = bankroll

    def add_bankroll(self, amount):
        self.bankroll += amount


sam = Player(bankroll=1000)

sam.add_bankroll(200)

print(sam.bankroll)


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit +  self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        # Aces can be 1 or 11 so need to define it here
        self.ace = False

    def __str__(self):
        """ Return a string of current hand composition """
        hand_comp = ""

        # Better way to do this ? List Comprehension?
        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name
        return "The hand has %s" %hand_comp

    def card_add(self, card):
        """Add another card to the hand"""
        self.cards.append(card)

        # Check for Aces
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):
        """ Calculate the value of the hand, make aces an 11 if they don't bust the hand"""
        if self.ace == True and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden == True and playing == True:
            # Don't show the first hidden card
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()

class Deck:
    def __init__(self):
        """ Create a deck in order"""
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        """ Shuffle the deck, python actually has a shuffle method in its random library"""
        random.shuffle(self.deck)

    def deal(self):
        """ Grab the first item in the deck"""
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()

        return "The deck has " + deck_comp

