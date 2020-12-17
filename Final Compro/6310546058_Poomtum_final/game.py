from card_deck import *
import random

class Player():
    """This class is for instantiating player instance
    """

    def __init__(self, name):
        """Creating Attributes
        """
        self.player_name = name
        self.player_hand = ""
        self.player_points = 0
        self.fund = 10000


class Dealer:
    def __init__(self):
        self.hand = ""


class Game:

    def __init__(self, player=2):
        deck = CardDeck()
        deck.shuffle()
        self.deck = deck
        self.players = [Player(str(i)) for i in range(player)]
        self.dealer = Dealer()

    def start(self):
        for i in self.players:
            i.player_hand = self.deck.draw_cards()
        self.dealer.hand = CardDeck.RANKS[random.randint(0,len(CardDeck.RANKS)-1)]
        for j in self.players:
            print(f"Player {j.player_name}: {j.fund}")
            bet_amount = int(input("Bet amount? : "))
            if bet_amount < j.fund:
                pass
            elif bet_amount > j.fund:
                print("Not enough fund!")
        for i in self.players:
            if CardDeck.RANKS.index(i.player_hand) > CardDeck.RANKS.index(self.dealer.hand):
                print(f"Player {i.player_name} wins!")
                i.player_points += 1
                i.fund += bet_amount
            elif CardDeck.RANKS.index(i.player_hand) == CardDeck.RANKS.index(self.dealer.hand):
                print("Tie")
            else:
                print(f"Player {i.player_name} loses!")
                i.player_points -= 1
                i.fund -= bet_amount
