class Player:
    def __init__(self,name,num_wins,num_plays):
        self.__name = name
        self.__num_wins = num_wins
        self.num_plays = num_plays
        self.hand = "None"

    def __str__(self):
        return "{0}: Wins = {1}: Plays = {2}: Hand = {3}".format(self.__name, self.__num_wins, self.num_plays,self.hand)

    def set_num_wins(self,num_wins):
        self.__num_wins = num_wins

    def set_name(self,name):
        self.__name = name

    def get_num_wins(self):
        return self.__num_wins
    
    def get_name(self):
        return self.__name

    def randomize_hand(self):
        import random
        x = random.randint(1, 3)
        if x == 1:
            self.hand = 'Rock'
        elif x == 2:
            self.hand = 'Paper'
        else:
            self.hand = 'Scissors'

