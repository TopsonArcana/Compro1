import random
from player import *
class Team:
    def __init__(self, filename,team_name='No Name'):
        self.__player_list = (self.__read_team(filename))
        self.__team_name = team_name
        self.__team_points = 0
        self.current_player = ""
    def __read_team(self, filename):
        player_list = []
        file = open(filename, "r")
        for i in file:
            player_list.append(Player(i.split(",")[0],int(i.split(",")[1]),int(i.split(",")[2].strip())))
        return player_list

    def __str__(self):
        return ("Team {0}\nTeam Points:{1}\n{2}").format(self.__team_name, self.__team_points,"\n".join([i.__str__() for i in self.__player_list]))

    def select_player(self):
        self.current_player = self.__player_list[random.randint(0, len(self.__player_list)-1)]
        self.current_player.randomize_hand()

    def update_team_points(self, value):
        if value == "win":
            self.__team_points += 1
            self.current_player.set_num_wins((self.current_player.get_num_wins()) + 1)
        self.current_player.num_plays = int(self.current_player.num_plays)
        self.current_player.num_plays += 1
        
    def get_team_points(self):
        return self.__team_points
    
    

