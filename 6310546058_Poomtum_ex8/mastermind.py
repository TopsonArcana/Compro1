from random import randint


class Game:
    def __init__(self):
        """Initializing a Game object which contain the randomized winning number
        >>> g = Game()
        >>> len(g.number) == 4
        True
        """
        self.color = ["1", "2", "3", "4", "5", "6"]
        self.number = ""
        for _ in range(4):
            self.number += str(self.color[randint(0, 5)])


class Player:
    def __init__(self):
        """Initializing a player instance
        >>> p = Player()
        >>> p.progress == ""
        True
        """
        self.progress = ""

    def check(self, guess, game):
        """Check and show how many guesses made correct
        >>> p = Player()
        >>> g = Game()
        >>> len(g.number)
        4
        >>> g.number = "2113"
        >>> p.check("1231",g)
        'oooo'
        >>> p.check(g.number,g)
        '****'
        """
        temp = [i for i in game.number]
        self.progress = ""
        for i in range(len(guess)):
            if guess[i] in temp:
                temp.remove(guess[i])
                if guess[i] == game.number[i]:
                    self.progress += "*"
                else:
                    self.progress += "o"
        return self.progress


