from whist.models.Player import Player
from whist.models.Game import Game


def new_game(players: str):
    while True:
        if not players:
            players = input(
                "Please insert the names of the 4 players, separated by a space:\n"
            )
        try:
            players = players.split()
            if len(players) != 4:
                raise ValueError("There must be 4 player names.")
            break
        except:
            print("Error while fetching players. Please try again")
            players = None
    players = [Player(name=player_name) for player_name in players]
    print()
    for i, player in enumerate(players):
        print(f"Player {i+1}: {player.name}")
    print()
    game = Game(players=players)
    while True:
        game.new_round()
