class CardDeck:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        """Create card deck
        """
        deck = []
        for rank in CardDeck.RANKS:
            card = rank
            deck += [card]
        self.card_deck = deck

    def shuffle(self):
        """Shuffle the deck of cards
        Args:
            None
        Returns:
            None
        """
        import random
        n = len(self.card_deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = self.card_deck[r]
            self.card_deck[r] = self.card_deck[i]
            self.card_deck[i] = temp

    def draw_cards(self):
        """Draw n card(s) from the deck
        >>> c = CardDeck()
        >>> len(c.draw_cards(1))
        1
        """
        draw = self.card_deck[-1]
        self.card_deck.remove(self.card_deck[-1])
        return draw
