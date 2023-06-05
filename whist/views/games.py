from whist.models.Player import Player
from whist.models.Game import (
    Game,
    Abondance,
    Troel,
    Solo,
    VragenEnMeegaan,
    KleineMiserie,
    GroteMiserie,
    GroteMiserieOpTafel,
    Piccolo,
    BaseMiserieClass,
)

import sys
import os
import json

from whist.constants import (
    KLEINE_MISERIE,
    KLEINE_SOLO_SLIM,
    GROTE_MISERIE,
    PICCOLO,
    GROTE_MISERIE_OP_TAFEL,
    GROTE_SOLO_SLIM,
    VRAGEN_EN_MEEGAAN,
    TROEL,
    SOLO,
    SOLO_POINT_SYSTEM,
    MISERIE_POINT_SYSTEM,
    ABONDANCE,
    ABONDANCE_POINT_SYSTEM,
    VRAGEN_EN_MEEGAAN_POINT_SYSTEM,
    GAME_TYPES,
    SAVE_FOLDER,
    TROEL_POINT_SYSTEM,
)


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
        new_round(game=game)


def new_round(game: Game) -> None:
    print()
    for index, item in enumerate(GAME_TYPES):
        print(f"({index})\t{item['name']}")
    while True:
        game_number = input("Select new game: ").strip()
        try:
            game_number = int(game_number)
        except Exception:
            print("Please insert a number.")
            continue
        if game_number in range(len(GAME_TYPES)):
            valid = False
            while True:
                validity = input(
                    f"Chosen game: '{GAME_TYPES[game_number]['name']}'. Is this correct? (Y/n): "
                ).strip()
                if validity in ("Y", "y", ""):
                    valid = True
                    break
                elif validity in ("N", "n"):
                    valid = False
                    break
                else:
                    continue
            if valid:
                break
            else:
                continue
        else:
            print("Please insert a valid number.")
            continue
    current_game_type = GAME_TYPES[game_number]
    while True:
        players = input(
            f"Who is playing {current_game_type['name']}? If more players, please separate with a space.\n(1)\t{game.players[0].name}\n(2)\t{game.players[1].name}\n(3)\t{game.players[2].name}\n(4)\t{game.players[3].name}\n\n(p)\tPrevious screen\n"
        ).strip()
        try:
            if players in ("P", "p"):
                return
            playing_players = players.split()
            for index, player in enumerate(playing_players):
                playing_players[index] = game.players[int(player) - 1]
            other_players = [x for x in game.players if x not in playing_players]
            if ABONDANCE in current_game_type["name"]:
                current_game = Abondance(
                    number_of_tricks=current_game_type["number_of_tricks"],
                    playing_players=playing_players,
                    other_players=other_players,
                )
            elif current_game_type["name"] == KLEINE_SOLO_SLIM:
                current_game = Abondance(
                    number_of_tricks=current_game_type["number_of_tricks"],
                    playing_players=playing_players,
                    other_players=other_players,
                )
            elif current_game_type["name"] == GROTE_SOLO_SLIM:
                current_game = Abondance(
                    number_of_tricks=current_game_type["number_of_tricks"],
                    playing_players=playing_players,
                    other_players=other_players,
                )
            elif VRAGEN_EN_MEEGAAN in current_game_type["name"]:
                current_game = VragenEnMeegaan(
                    number_of_tricks=current_game_type["number_of_tricks"],
                    playing_players=playing_players,
                    other_players=other_players,
                )
            elif current_game_type["name"] == TROEL:
                current_game = Troel(
                    number_of_tricks=current_game_type["number_of_tricks"],
                    playing_players=playing_players,
                    other_players=other_players,
                )
            elif SOLO in current_game_type["name"]:
                current_game = Solo(
                    number_of_tricks=current_game_type["number_of_tricks"],
                    playing_players=playing_players,
                    other_players=other_players,
                )
            elif current_game_type["name"] == KLEINE_MISERIE:
                current_game = KleineMiserie(
                    playing_players=playing_players, other_players=other_players
                )
            elif current_game_type["name"] == GROTE_MISERIE:
                current_game = GroteMiserie(
                    playing_players=playing_players, other_players=other_players
                )
            elif current_game_type["name"] == PICCOLO:
                current_game = Piccolo(
                    playing_players=playing_players, other_players=other_players
                )
            elif current_game_type["name"] == GROTE_MISERIE_OP_TAFEL:
                current_game = GroteMiserieOpTafel(
                    playing_players=playing_players, other_players=other_players
                )
            break
        except Exception as e:
            print(e)
            print("Could not parse input. Please try again.")

    if issubclass(type(current_game), BaseMiserieClass):
        current_game.complete()
        current_game.assign_points()
    else:
        while True:
            answer = input("How many tricks were achieved? ").strip()
            try:
                answer = int(answer)
                if answer not in range(1, 14):
                    continue
                break
            except Exception:
                continue
        current_game.assign_points(tricks_achieved=answer)
    print("Adding scores to scoresheet...")
    game.add_record_to_scoresheet()
    game.display_points()
    while True:
        answer = input("(N)ext round | (S)ave | (Q)uit: ").strip()
        if answer in ("N", "n"):
            break
        elif answer in ("S", "s"):
            game.save()
        elif answer in ("Q", "q"):
            sys.exit(0)
        else:
            continue

    print("Starting new round...")
    game.current_round += 1


def load_game():
    print(f"{os.listdir(SAVE_FOLDER)}")
    answer = input("Please select a game to load: ").strip()
    with open(f"{SAVE_FOLDER}{answer}", "r") as f:
        payload = json.load(f)
    players = []
    for index, item in enumerate(payload["players"]):
        players.append(Player(name=item, score=payload["scoresheet"][-1][index]))
    game = Game(
        current_round=payload["current_round"],
        scoresheet=payload["scoresheet"],
        players=players,
    )
    while True:
        new_round(game=game)
