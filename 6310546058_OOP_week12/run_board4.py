from Board import *
from player import *
import random

board = Board('board3.txt')
a = Player('A')
b = Player('B')
board.add_player(a)
board.add_player(b)
print('Starting...')
print(board)
round = 1
whofirst = random.randint(1, 2)
while True:
    print('>>> Round ' + str(round))
    if whofirst == 1:
        player = a
        player.randomize_dice()
        print(player.name + '\'s position = ' + str(player.current_pos) + '. ', end='')
        print(player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        player = b
        player.randomize_dice()
        print(player.name + '\'s position = ' + str(player.current_pos) + '. ', end='')
        print(player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        round += 1
        if board.check_winner():
            print(board.get_winner())
            break
    else:
        player = b
        player.randomize_dice()
        print(player.name + '\'s position = ' + str(player.current_pos) + '. ', end='')
        print(player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        player = a
        player.randomize_dice()
        print(player.name + '\'s position = ' + str(player.current_pos) + '. ', end='')
        print(player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        round += 1
        if board.check_winner():
            print(board.get_winner())
            break
