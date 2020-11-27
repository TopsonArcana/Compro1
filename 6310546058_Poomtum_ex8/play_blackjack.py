from blackjack import *

game = Blackjack()
game.start()
i = 1
for player in game.players:
    if player.player_hand_value == 21:
        print("Blackjack!")
        game.decision()
        exit()
for player in game.players:
    print(f"Player {i}")
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
game.decision()


