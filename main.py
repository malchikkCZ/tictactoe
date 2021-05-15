from engine import *
from players import *
    
is_game_on = True

while is_game_on:

    players = [Player("X")]
    second = input("Second player is (H)uman, (E)asy or (A)dvanced? >>> ").lower()
    
    if second == "h":
        players.append(Player("O"))
    elif second == "a":
        players.append(HardComputer("O"))
    else:
        players.append(EasyComputer("O"))

    print()
    board = Board()
    game = Game(board, players)

    game.game_on()

    again = input("Do you want to play again? (Y/n) >>> ").lower()
    if again == "n":
        is_game_on = False
