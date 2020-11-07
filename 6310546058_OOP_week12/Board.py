from cell import *


class Board:
    def __init__(self, filename):
        self.__width = 0
        self.__length = 0
        self.__cell_list = self.__read_board(filename)

    @property
    def cell_list(self):
        return self.__cell_list

    def __read_board(self, filename):
        celllist = []
        f = open(filename, "r")
        self.__width = f.readline().strip()
        self.__length = f.readline().strip()
        for i in f.readlines():
            celllist.append(Cell(i.split(",")[0], i.split(",")[1], i.split(",")[2].strip()))
        return celllist

    def add_player(self, player):
        self.__cell_list[0].add_occupy_list(player)

    def access_cell(self, cell_id):
        return self.__cell_list[int(cell_id)]

    def check_winner(self):
        if self.access_cell(self.cell_list[-1].id).get_occupy_list_str() == "":
            return False
        else:
            return True

    def get_winner(self):
        if self.check_winner():
            return "Game Over. {0} wins".format(self.access_cell(self.cell_list[-1].id).occupy_list[0].name)
        else:
            return None

    def update_board(self, player):
        if player.current_hold == True:
            pass
        else:
            self.access_cell(player.current_pos).remove_occupy_list(player)
            player.move(self)
            player.obtain_cell_status(self)
            self.access_cell(player.current_pos).add_occupy_list(player)

    def __str__(self):
        return "".join(["""
- - - - - - - -
|      {0:3}     |
|   {1:3}, {2:5} |
|     {3:4}     |""".format(i.id, i.move, i.hold, i.get_occupy_list_str()) for i in self.__cell_list])
