#card

#value
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {  "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, 
            "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, 
            "Queen":12, "King":13, "Ace":14
        }

# CARD
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# DECK
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #membuat objek baru dari class Card
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# new_deck = Deck()

# shuffle
# new_deck.shuffle()
# print(new_deck.all_cards[1])

# prinnt all cards
# for card_object in new_deck.all_cards:
#     print(card_object)

# PLAYER
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.value = 0
        self.aces = 0
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # Daftar kartu yang diberikan
            self.all_cards.extend(new_cards)
        else:
            # satu kartu yang diberikan
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards with value {self.value}"

# new_player = Player("Abi")

# GAME SETUP
player_one = Player("Abi")
player_two = Player("Iba")

new_deck = Deck()
new_deck.shuffle()

# SPLIT DECK
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

# WHILE GAME ON
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    # jika pemain 1 kehabisan kartu makan pemain 2 menang
    if len(player_one.all_cards) == 0:
        print('Player One out of cards. Player Two wins!')
        game_on = False
        break
    # jika pemain 2 kehabisan kartu makan pemain 1 menang
    if len(player_two.all_cards) == 0:
        print('Player Two out of cards. Player One wins!')
        game_on = False
        break

    # New Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
