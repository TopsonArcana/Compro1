from mastermind import *

game = Game()
player = Player()
round = 1
game.number = "1111"
while True:
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