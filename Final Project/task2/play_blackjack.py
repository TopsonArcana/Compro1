from blackjack import *
from random import randint
game = Blackjack()
for i in game.players:
    i.player_name = game.player_info[randint(0,len(game.player_info)-1)][0]
game.start()
i = 1
for player in game.players:
    if player.player_hand_value == 21:
        print("Blackjack!")
        game.decision()
        exit()
for player in game.players:
    print(f"{player.player_name}")
    while player.player_hand_status == "must_draw_more":
        game.adjust_player_hand(player)
        Blackjack.display_player_hand(player)
    if player.player_hand_status == "can_stay":
        Blackjack.display_player_hand(player)
        choice = input("stay or not: ")
        if choice == "not":
            game.adjust_player_hand(player)
            Blackjack.display_player_hand(player)
        else:
            player.player_hand_status = "stay"
    i += 1
while game.computer.player_hand_status != 'can_stay':
    game.adjust_player_hand(game.computer)
    Blackjack.display_player_hand(game.computer)
while game.computer.player_hand_value < game.players[0].player_hand_value and game.computer.player_hand_value < game.players[1].player_hand_value and game.computer_hand_status == 'can_stay':
    game.adjust_player_hand()
    Blackjack.display_player_hand()
game.decision()
for number,player in enumerate(game.players):
    print(f"{player.player_name} {number+1}: " + str(Blackjack.show_score(player)))
print("Computer : " + str(Blackjack.show_score(game.computer)))
