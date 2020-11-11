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
        self.__width = int(f.readline().strip())
        self.__length = int(f.readline().strip())
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
            return "Game Over! {0} wins".format(self.access_cell(self.cell_list[-1].id).occupy_list[0].name)
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
        display = []
        for row in range(self.__length):
            if (row % 2) == 0:
                display.append("- - - - - - -  " * self.__width)
                display.append("".join([f"|      {i.id:3}     |"
                                if self.__cell_list.index(i) == (row + 1) * (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                else f"|      {i.id:3}     "
                                for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]]))
                display.append("".join([f"|   {i.move:3},{i.hold:5}  |"
                                if self.__cell_list.index(i) == (row + 1) * (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                else f"|   {i.move:3},{i.hold:5}  "
                                for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]]))
                display.append("".join([f"|      {i.get_occupy_list_str():3}     |"
                                if self.__cell_list.index(i) == (row + 1) * (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                else f"|     {i.get_occupy_list_str():6}   "
                                for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]]))
            else:
                display.append("- - - - - - -  " * self.__width)
                display.append("".join(reversed([f"|      {i.id:3}     |"
                                if self.__cell_list.index(i) == (row + 1) * (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                else f"      {i.id:3}     |"
                                for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]])))
                display.append("".join(reversed([f"|   {i.move:3},{i.hold:5}  |"
                                if self.__cell_list.index(i) == (row + 1) * (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                else f"   {i.move:3},{i.hold:5}  |"
                                for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]])))
                display.append("".join(reversed([f"|      {i.get_occupy_list_str():3}     |"
                                if self.__cell_list.index(i) == (row + 1) * (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                else f"     {i.get_occupy_list_str():6}   |"
                                for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]])))
        if row == self.__length - 1:
            display.append(" - - - - - - - " * self.__width)
        return "\n".join(display)
