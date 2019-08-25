import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(rank + ' of ' + suit)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        sample = random.sample(self.deck, 2)
        for char in sample:
            sample.remove(char)

    def __str__(self):
        return str(self.deck)


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0

    def add_card(self, card):
        self.value += values[card.split()[0]]
        self.cards.append(card)
        if card.split()[0] == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


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
    x = deck.deck.pop()
    hand.add_card(x)


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input('Do you want to hit or stand? ').lower()
        if x == 'hit' or x == 'stand':
            break
    if x == 'hit':
        hit(deck, hand)
    if x == 'stand':
        playing = False


def show_some(dealer, player):
    print("\nDealer's cards")
    print('First card hidden!')
    for cards in dealer[1:]:
        print(cards)
    print("\nPlayer's cards")
    for sec_cards in player:
        print(sec_cards)


def show_all(dealer,player):
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


print('\n'*100+'Welcome to Black Jack!')
while True and chips.total != 0:
    the_deck = Deck()
    the_deck.shuffle()
    playcards = the_deck.deal()
    dealcards = the_deck.deal()
    print(f'You currently have {chips.total} chips!')
    take_bet()
    for cards in playcards:
        player.add_card(cards)
    for crds in dealcards:
        dealer.add_card(crds)
    while playing:
        show_some(dealer.cards, player.cards)
        hit_or_stand(the_deck, player)
        if player_busts():
            player.adjust_for_ace()
            if player_busts():
                chips.lose_bet()
                show_all(dealer.cards,player.cards)
                print('PLAYER BUSTED! Dealer wins')
                break

    while True and not player_busts():
        if dealer.value > player.value:
            break
        if dealer.value >= 17:
            break
        hit(the_deck, dealer)
        if dealer_busts():
            dealer.adjust_for_ace()
            if dealer_busts():
                chips.win_bet()
                show_all(dealer.cards,player.cards)
                print('DEALER BUSTED! Player wins!')
                break
    if player_busts() == False and dealer_busts() == False:
        show_all(dealer.cards, player.cards)
        if player_wins():
            chips.win_bet()
            print('Player Wins!')
        if dealer_wins():
            chips.lose_bet()
            print('Sorry dealer wins')
        if push():
            print('Tie!')

    print(f'You currently have {chips.total} chips\n')

    if chips.total != 0:
        replay = input('Do you want to play another round, yes or no\n').lower()
        if replay == 'yes':
            player.value = 0
            dealer.value = 0
            player.cards.clear()
            dealer.cards.clear()
            playing = True
            continue
        else:
            break
