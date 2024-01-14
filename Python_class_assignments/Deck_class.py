import random

class Deck:
    valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ['H', 'D', 'C', 'S']
    
    def __init__(self):
        self.valid_cards = []
        self.fill_deck()

    def fill_deck(self):
        for value in Deck.valid_values:
            for suit in Deck.valid_suits:
                card = value + suit
                self.valid_cards.append(card)
    
    def copy(self):
        new_deck = Deck()
        new_deck.valid_cards = self.valid_cards[:]
        return new_deck
    
    def shuffle(self):
        random.shuffle(self.valid_cards)
    
    def deal(self, n):
        deal_deck = []
        if n < len(self.valid_cards):
            i = 0
            for i in range(n):
                deal_deck.append(self.valid_cards[-1])
                self.valid_cards.pop()
                i += 1
            return deal_deck
        else:
            deal_deck = self.valid_cards
            return deal_deck
        
    def contains(self, card):
        if card in self.valid_cards:
            return True
        else:
            return False

    def get_cards(self):
        return self.valid_cards[:]
    
    def __len__(self):
        return len(self.valid_cards)

    def sort_by_suit(self):
        list_hearts = []
        list_diamonds = []
        list_clubs = []
        list_spades = []

        for card in self.valid_cards:
            suit = card[-1]
            if suit == "H":
                list_hearts.append(card)
            if suit == "D":
                list_diamonds.append(card)
            if suit == "C":
                list_clubs.append(card)
            if suit == "S":
                list_spades.append(card)
        
        self.valid_cards = list_hearts + list_diamonds + list_clubs + list_spades

