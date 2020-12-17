from game import *
num_player = int(input("How many players: "))
game = Game(num_player)
session = 0
while session != 5:
    print(f"Session {session}")
    game.start()
    for j in game.players:
        print(f"Player {j.player_name} hand: {j.player_hand}")
    print("")
    for j in game.players:
        print(f"Player {j.player_name} points: {j.player_points}")
    session += 1
    print("")