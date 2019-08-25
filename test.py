import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + 'of' + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(rank + ' of ' + suit)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return random.sample(self.deck, 2)

    def __str__(self):
        return str(self.deck)


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.value += values[card.split()[0]]
        self.cards.append(card)

    def adjust_for_ace(self):
        for char in self.cards:
            if 'Ace' in char:
                self.aces += 1
                self.value -= 11
                self.value += 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


chips = Chips()


def take_bet():
    while True:
        chips.bet = int(input('How much do you want to bet: '))
        if 0 < chips.bet <= chips.total:
            break


def hit(deck, hand):
    while hand.value < 21:
        x = random.choice(deck.deck)
        hand.add_card(x)


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    x = input('Do you want to hit or stand? ').lower()
    if x == 'hit':
        hit(deck, hand)
    else:
        playing = False


def show_some(player,dealer):
    print("\nDealer's cards")
    print('First card hidden!')
    for cards in dealer[1:]:
        print(cards)
    print("\nPlayer's cards")
    for sec_cards in player:
        print(sec_cards)


def show_all(player,dealer):
    print("\nDealer's cards")
    for cards in dealer:
        print(cards)
    print("\nPlayer's cards")
    for sec_cards in player:
        print(sec_cards)


player = Hand()
dealer = Hand()


def player_busts():
    return player.value > 21


def player_wins():
    return player.value > dealer.value


def dealer_busts():
    return dealer.value > 21


def dealer_wins():
    return dealer.value > player.value


def push():
    return dealer.value == player.value


while True:
    the_deck = Deck()
    the_deck.shuffle()
    playcards = the_deck.deal()
    dealcards = the_deck.deal()
    for cards in playcards:
        player.add_card(cards)
    for crds in dealcards:
        dealer.add_card(crds)
    print(player.cards)
    hit_or_stand(the_deck, player)
    print(player.cards)
    break