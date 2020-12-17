class Football:
    def __init__(self, name="", short_name="", wins=0, draws=0, loses=0):
        self.__team_name = name
        self.__team_short = short_name
        self.__num_wins = wins
        self.__num_draws = draws
        self.__num_loses = loses

    @property
    def win(self):
        return self.__num_wins

    @win.setter
    def win(self, value):
        self.__num_wins = value

    @property
    def draw(self):
        return self.__num_draws
    @draw.setter
    def draw(self,value):
        self.__num_draws = value

    @property
    def lose(self):
        return self.__num_loses

    @lose.setter
    def lose(self, value):
        self.__num_loses = value

    def __str__(self):
        return f"{self.__team_name},{self.__team_short},{self.__num_wins},{self.__num_draws},{self.__num_loses}"

    def won(self,team):
        self.__num_wins += 1
        team.__num_loses += 1

    def drew(self,team):
        self.__num_draws += 1
        team.__num_draws += 1

    def losed(self,team):
        self.__num_loses += 1
        team.__num_wins += 1


