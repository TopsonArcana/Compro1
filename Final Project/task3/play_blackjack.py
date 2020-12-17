from blackjack import *

def menu():
    num_player = int(input("How many players? "))
    game = Blackjack(num_player)
    for i in game.players:
            print(i.player_name)
    while True:
        choice = int(input(
            ">>>Main menu\n1.Play game\n2.Add player's budget\n3.View player's profile\n4.View stat\n5.Quit program\nEnter menu choice: "))
        if choice == 1:
            play_bj(game)
        elif choice == 2:
            add_budget(game)
        elif choice == 3:
            print(view_player(game))
        elif choice == 4:
            stat(game)
        elif choice == 5:
            exit()


def play_bj(game):
    game.start()
    i = 1
    for player in game.players:
        if player.player_hand_value == 21:
            print("Blackjack!")
            game.decision()
            exit()
        player.budget -= 100
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
    while game.computer.player_hand_value < game.players[0].player_hand_value and game.computer.player_hand_value < \
            game.players[1].player_hand_value and game.computer_hand_status == 'can_stay':
        game.adjust_player_hand()
        Blackjack.display_player_hand()
    game.decision()
    for number, player in enumerate(game.players):
        print(f"{player.player_name} {number + 1}: " + str(Blackjack.show_score(player)))
    print("Computer : " + str(Blackjack.show_score(game.computer)))


def add_budget(game):
    player = input("Enter player's name: ")
    budget = int(input("Enter added budget: "))
    for i in game.players:
        if i.player_name == player:
            i.budget += budget
            print(f"{budget} Added")
            print(
                f"{i.player_name}, {i.gender}, {i.region}\nBudget = {i.budget}\nNumber of wins = {i.num_wins}\nNumber of losses = {i.num_loses}")


def view_player(game):
    player = input("Enter player's name: ")
    for i in game.players:
        if i.player_name == player:
            return f"{i.player_name}, {i.gender}, {i.region}\nBudget = {i.budget}\nNumber of wins = {i.num_wins}\nNumber of losses = {i.num_loses}"


def stat(game):
    game.player_info.sort(key=lambda x: x[4], reverse=True)
    rank = 1
    for i in game.player_info[:5]:
        print(f"{rank}.{i[0]}, {i[1]}, {i[2]}\nBudget = {i[3]}\nNumber of wins = {i[4]}\nNumber of losses = {i[5]}")
        rank += 1

menu()