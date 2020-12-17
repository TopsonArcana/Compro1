from card_deck import *


class Player():
    """This class is for instantiating player instance
    """

    def __init__(self):
        """Creating Attributes
        """
        self.player_hand = []
        self.player_hand_value = 0
        self.player_hand_status = ""
        self.player_points = 0


class Blackjack:
    """Class containing all the method to operate a blackjack game
    """

    def __init__(self):
        deck = CardDeck()
        deck.shuffle()
        self.bj_deck = deck
        self.players = [Player() for i in range(2)]
        self.computer = Player()

    def start(self):
        """Start game and set up players hand and value
        >>> b = Blackjack()
        >>> b.start()
        >>> len(b.players[0].player_hand)
        2
        >>> b.players[1].player_hand_value != 0
        True
        """
        for i in self.players:
            i.player_hand = self.bj_deck.draw_cards(2)
            Blackjack.value_cal(i)
            Blackjack.status_update(i)

    @staticmethod
    def status_update(player):
        """Update status of a player whether they've to draw or they can stay
        Args:
            player(object): [Player of blackjack game]
        """
        if player.player_hand_value < 16:
            player.player_hand_status = "must_draw_more"
        else:
            player.player_hand_status = "can_stay"

    @staticmethod
    def value_cal(player):
        """Calculate the value of player hand

        Args:
            player (object): [Player of blackjack game]
        """
        ace = 0
        player.player_hand_value = 0
        for i in player.player_hand:
            if i[0] == "A":
                ace += 1
                player.player_hand_value += 1
            try:
                player.player_hand_value += int(i.split()[0])
            except:
                player.player_hand_value += 10
        Blackjack.ace_cal(player, ace)

    @staticmethod
    def ace_cal(player, num_ace):
        """Calculate whether ace should be 1 or 11

        Args:
            player (object): [Player of blackjack game]
            num_ace (int): [number of ace]
        """
        while num_ace > 0:
            if player.player_hand_value + 10 <= 21:
                player.player_hand_value += 10
            num_ace -= 1

    def adjust_player_hand(self, player):
        """Draw additional card and reevaluate value

        Args:
            player (object): [Player of blackjack game]
        """
        player.player_hand.extend(self.bj_deck.draw_cards(1))
        Blackjack.value_cal(player)
        Blackjack.status_update(player)

    @staticmethod
    def display_player_hand(player):
        """Print player hand

        Args:
            player (object): [Player of blackjack game]
        """
        print(" ".join(player.player_hand))

    def decision(self):
        """This method makes a decision if the player wins, looses, or ties with the computer
        """
        if (self.players[0].player_hand_value > 21) and (self.players[1].player_hand_value < 21):
            print("Player 2 win")
        elif (self.players[0].player_hand_value < 21) and (self.players[1].player_hand_value > 21):
            print("Player 1 win")
        elif self.players[0].player_hand_value > self.players[1].player_hand_value:
            print("Player 1 win")
        elif self.players[0].player_hand_value < self.players[1].player_hand_value:
            print("Player 2 win")
        else:
            print("Tie")
