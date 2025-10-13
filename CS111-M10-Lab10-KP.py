# Constants for Procedural Approach
DECK = 0
HAND = 1
COMPUTER = 2
CARD_NAMES = (
    "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Jack", "Queen", "King"
)
SUIT_NAMES = ("Clubs", "Diamonds", "Hearts", "Spades")

import random

# Procedural Approach
def initCards():
    """Initialize a list of 52 integers, all set to DECK (0)."""
    return [DECK for _ in range(52)]

def cardName(index):
    """Return the string name of the card at the given index."""
    rank = index % 13
    suit = index // 13
    return f"{CARD_NAMES[rank]} of {SUIT_NAMES[suit]}"

def assignCard(cardDB, hand):
    """Assign a random card from the deck to the specified hand."""
    available_cards = [i for i, loc in enumerate(cardDB) if loc == DECK]
    if not available_cards:
        return False
    card_index = random.choice(available_cards)
    cardDB[card_index] = hand
    return True

def showDB(cardDB):
    """Print each card’s index, name, and location."""
    locations = {DECK: "Deck", HAND: "Player Hand", COMPUTER: "Computer Hand"}
    for i, loc in enumerate(cardDB):
        print(f"Index {i:2d}: {cardName(i):20} Location: {locations[loc]}")

def showHand(cardDB, hand):
    """Print all cards in the specified hand."""
    print(f"\nHand {hand}:")
    for i, loc in enumerate(cardDB):
        if loc == hand:
            print(cardName(i))

# OOP Approach
class Card:
    """Represents a single playing card with rank and suit."""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{CARD_NAMES[self.rank]} of {SUIT_NAMES[self.suit]}"

class Deck:
    """Represents a deck of 52 cards with methods to shuffle and deal."""
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in range(4) for rank in range(13)]
    
    def shuffle(self):
        """Shuffle the deck using random.shuffle."""
        random.shuffle(self.cards)
    
    def deal_card(self):
        """Deal one card from the deck if available."""
        return self.cards.pop() if self.cards else None
    
    def cards_left(self):
        """Return the number of cards remaining in the deck."""
        return len(self.cards)

class Hand:
    """Represents a player's hand of cards."""
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        """Add a card to the hand."""
        if card:
            self.cards.append(card)
    
    def show_hand(self):
        """Print all cards in the hand."""
        for card in self.cards:
            print(card)

class Player:
    """Represents a player with a name and a hand of cards."""
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
    
    def add_card(self, card):
        """Add a card to the player's hand."""
        self.hand.add_card(card)
    
    def show_hand(self):
        """Print the player's hand."""
        print(f"\n{self.name}'s Hand:")
        self.hand.show_hand()

def main_procedural():
    """Main function for procedural approach demonstration."""
    print("Procedural Approach Demo:")
    cardDB = initCards()
    
    # Deal 5 cards to player hand
    for _ in range(5):
        assignCard(cardDB, HAND)
    
    # Deal 5 cards to computer hand
    for _ in range(5):
        assignCard(cardDB, COMPUTER)
    
    # Show entire database
    showDB(cardDB)
    
    # Show individual hands
    showHand(cardDB, HAND)
    showHand(cardDB, COMPUTER)

def main_oop():
    """Main function for OOP approach demonstration."""
    print("\nOOP Approach Demo:")
    # Create and shuffle deck
    deck = Deck()
    deck.shuffle()
    
    # Create players
    player = Player("Player")
    computer = Player("Computer")
    
    # Deal 5 cards to each player
    for _ in range(5):
        player.add_card(deck.deal_card())
        computer.add_card(deck.deal_card())
    
    # Show hands
    player.show_hand()
    computer.show_hand()
    
    # Show remaining cards in deck
    print(f"\nCards left in deck: {deck.cards_left()}")

if __name__ == "__main__":
    main_procedural()
    main_oop()