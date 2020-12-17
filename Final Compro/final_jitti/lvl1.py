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
    def draw(self, value):
        self.__num_draws = value

    @property
    def lose(self):
        return self.__num_loses

    @lose.setter
    def lose(self, value):
        self.__num_loses = value

    def __str__(self):
        return f"{self.__team_name},{self.__team_short},{self.__num_wins},{self.__num_draws},{self.__num_loses}"


ARS = Football("ARS", "Arsenal")
print(ARS)
ARS.win = 1
print(ARS)
ARS.draw = 4
print(ARS)
ARS.lose = 2
print(ARS)
print(ARS.win)
print(ARS.draw)
print(ARS.lose)
