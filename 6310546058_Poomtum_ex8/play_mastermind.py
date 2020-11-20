from mastermind import *

game = Game()
player = Player()
round = 1
while True:
    print(game.number)
    number = input("What is your guess?: ")
    print(f"Your guess is {number}")
    player.check(number, game)
    print(player.progress)
    if player.progress == "****":
        print(f"You solved it after {round} rounds")
        break
    else:
        pass
    round += 1