# This code creates a random poker head with five cards then replaces the cards the user wants to replace.
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        suits = {0: 'Clubs', 1: 'Diamonds', 2: 'Hearts', 3: 'Spades'}
        ranks = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King'}
        return f"{ranks[self.rank]} of {suits[self.suit]}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, num_cards):
        hand = []
        for _ in range(num_cards):
            if self.cards:
                hand.append(self.cards.pop())
            else:
                print("Not enough cards in the deck to deal.")
                break
        return hand

def print_hand(hand):
    print("\nYour current hand:")
    for i, card in enumerate(hand):
        print(f"{i+1}. {card}")

def get_cards_to_replace():
    while True:
        try:
            selection_str = input("Enter the numbers of the cards to replace (e.g., 1, 3, 5), or press Enter to keep all: ")
            if not selection_str:
                return []
            selected_indices = [int(x.strip()) - 1 for x in selection_str.split(',')]
            if all(0 <= i < 5 for i in selected_indices):
                return selected_indices
            else:
                print("Invalid card number. Please enter numbers between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

def play_poker():
    deck = Deck()
    hand = deck.deal_cards(5)
    print_hand(hand)

    indices_to_replace = get_cards_to_replace()

    for index in sorted(indices_to_replace, reverse=True):
        if 0 <= index < len(hand):
            hand.pop(index)

    new_cards = deck.deal_cards(len(indices_to_replace))
    hand.extend(new_cards)

    print("\nYour hand after the draw:")
    print_hand(hand)

if __name__ == "__main__":
    play_poker()