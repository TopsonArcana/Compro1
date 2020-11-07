from team import *
#8
# team_a = Team('team_a.txt','A')
# print(team_a)
# team_b = Team('team_b.txt','B')
# print(team_b)

#9
# team_a = Team('team_a.txt','A')
# print(team_a)
# team_b = Team('team_b.txt','B')
# print(team_b)
# team_a.select_player()
# print(team_a.current_player)
# team_b.select_player()
# print(team_b.current_player)

#10
def find_winner(first_player, second_player):
    if first_player.hand == second_player.hand:
        return 0
    elif first_player.hand == "Rock" and second_player.hand == "Scissors":
        return 1
    elif first_player.hand == "Scissors" and second_player.hand == "Paper":
        return 1
    elif first_player.hand == "Paper" and second_player.hand == "Rock":
        return 1
    elif second_player.hand == "Rock" and first_player.hand == "Scissors":
        return 2
    elif second_player.hand == "Scissors" and first_player.hand == "Paper":
        return 2
    elif second_player.hand == "Paper" and first_player.hand == "Rock":
        return 2
# team_a = Team('team_a.txt','A')
# print(team_a)
# team_b = Team('team_b.txt','B')
# print(team_b)
# team_a.select_player()
# print(team_a.current_player)
# team_b.select_player()
# print(team_b.current_player)
# winning_team = find_winner(team_a.current_player,
# team_b.current_player)
# print(winning_team)

#11
# team_a = Team('team_a.txt','A')
# print(team_a)
# team_b = Team('team_b.txt','B')
# print(team_b)
# team_a.select_player()
# print(team_a.current_player)
# team_b.select_player()
# print(team_b.current_player)
# team_a.update_team_points('win')
# print(team_a)
# team_b.update_team_points('lose')
# print(team_b)
    
#12
def update_points(winning_team, first_team, second_team):
    if winning_team == 1:
        print("A wins.")
        first_team.update_team_points('win')
    elif winning_team == 2:
        print("B wins.")
        second_team.update_team_points('win')
    else:
        print("Both team tie") 
# team_a = Team('team_a.txt','A') 
# print(team_a)
# team_b = Team('team_b.txt','B')
# print(team_b)
# team_a.select_player()
# print(team_a.current_player)
# team_b.select_player()
# print(team_b.current_player)
# winning_team = find_winner(team_a.current_player,team_b.current_player)
# print(winning_team)
# update_points(winning_team, team_a, team_b)
# print(team_a)
# print(team_b)

#13
team_a = Team('team_a.txt','A') 
team_b = Team('team_b.txt','B')
while True:
    team_a.select_player()
    print(team_a.current_player)
    team_b.select_player()
    print(team_b.current_player)
    winning_team = find_winner(team_a.current_player,team_b.current_player)
    print(winning_team)
    update_points(winning_team, team_a, team_b)
    print(team_a)
    print(team_b)
    if (team_a.get_team_points() == 5) or (team_b.get_team_points() == 5):
        break

