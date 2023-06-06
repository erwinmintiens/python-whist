from typing import Union
import json
import sys
import os
from colorama import Fore, Style
from whist.models.Player import Player
from whist.models.RoundTypes import (
    BaseMiserieClass,
    Abondance,
    VragenEnMeegaan,
    Solo,
    GroteMiserie,
    KleineMiserie,
    GroteMiserieOpTafel,
    Troel,
    Piccolo,
)

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
    ABONDANCE,
    GAME_TYPES,
    SAVE_FOLDER,
)


class Game:
    def __init__(
        self,
        current_round: int = 1,
        players: list = [None, None, None, None],
        scoresheet: list = [],
        current_game_id: Union[None, int] = None,
    ):
        self.current_round = current_round
        self.players = players
        self.scoresheet = scoresheet
        self.current_game_id = current_game_id

    def display_points(self):
        print()
        print(
            f"\t|{self.players[0].name}\t|{self.players[1].name}\t|{self.players[2].name}\t|{self.players[3].name}"
        )
        print("\t|-----\t|-----\t|-----\t|-----")
        for i, record in enumerate(self.scoresheet):
            print(f"{i+1}\t|{record[0]}\t|{record[1]}\t|{record[2]}\t|{record[3]}")
        print()

    def add_record_to_scoresheet(self) -> None:
        self.scoresheet.append(
            (
                self.players[0].score,
                self.players[1].score,
                self.players[2].score,
                self.players[3].score,
            )
        )

    def menu(self):
        while True:
            print()
            answer = input(
                f"({Fore.BLUE}N{Style.RESET_ALL})ext round | ({Fore.BLUE}S{Style.RESET_ALL})ave | ({Fore.BLUE}D{Style.RESET_ALL})isplay scoresheet | ({Fore.BLUE}Q{Style.RESET_ALL})uit: "
            ).strip()
            if answer in ("N", "n"):
                break
            elif answer in ("S", "s"):
                self.save()
            elif answer in ("Q", "q"):
                while True:
                    quitting = input("Are you sure you wish to exit? (y/N): ").strip()
                    if quitting in ("N", "n", ""):
                        break
                    elif quitting in ("Y", "y"):
                        sys.exit(0)
                    else:
                        continue
            elif answer in ("D", "d"):
                self.display_points()
            else:
                continue

    def save(self):
        payload = {
            "current_round": self.current_round,
            "scoresheet": self.scoresheet,
            "players": [player.name for player in self.players],
        }
        while True:
            answer = input("Give a name for the file (leave empty to cancel): ").strip()
            if answer == "":
                print(
                    f"{Fore.RED}You provided an empty value. Game not saved.{Style.RESET_ALL}"
                )
                break
            try:
                with open(f"{SAVE_FOLDER}{answer}.json", "w") as f:
                    json.dump(payload, f, indent=2)
                print(
                    f"{Fore.GREEN}Successfully saved to {SAVE_FOLDER}{answer}.json{Style.RESET_ALL}"
                )
                break
            except Exception as e:
                print(e.__repr__())
                continue

    def new_game(self):
        while True:
            players = input(
                "Please insert the names of the 4 players, all separated by a space:\n"
            )
            try:
                players = players.split()
                if len(players) != 4:
                    raise ValueError("There must be exactly 4 player names.")
                break
            except Exception as e:
                print(
                    f"{Fore.RED}Error while fetching players: {e} Please try again.{Style.RESET_ALL}"
                )
                players = None
        players = [Player(name=player_name) for player_name in players]
        print()
        for i, player in enumerate(players):
            print(f"Player {i+1}: {player.name}")
        print()
        self.players = players
        self.new_round()

    def load_game(self):
        while True:
            json_files = [
                pos_json
                for pos_json in os.listdir(SAVE_FOLDER)
                if pos_json.endswith(".json")
            ]
            print()
            for index, name in enumerate(json_files):
                print(f"({Fore.BLUE}{index}{Style.RESET_ALL})\t{name}")
            answer = input("Please select a game to load: ").strip()
            try:
                try:
                    answer = int(answer)
                except Exception:
                    raise TypeError("Please provide a valid number.")
                if answer not in range(len(json_files)):
                    raise ValueError("Please select a valid number.")
                with open(f"{SAVE_FOLDER}{json_files[answer]}", "r") as f:
                    payload = json.load(f)
                break
            except Exception as e:
                print()
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
                print()
                continue
        players = []
        for index, item in enumerate(payload["players"]):
            players.append(Player(name=item, score=payload["scoresheet"][-1][index]))
        self.current_round = payload["current_round"]
        self.scoresheet = payload["scoresheet"]
        self.players = players
        self.new_round()

    def new_round(self):
        while True:
            self.display_points()
            self.menu()

            print(f"{Fore.GREEN}Starting new round...{Style.RESET_ALL}")
            current_game_type = choose_game_type()
            current_game = choose_players(
                game=self, current_game_type=current_game_type
            )
            if not current_game:
                continue

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
            self.add_record_to_scoresheet()
            self.current_round += 1


def choose_game_type() -> dict:
    print("-" * 30)
    for index, item in enumerate(GAME_TYPES):
        print(f"({Fore.BLUE}{index}{Style.RESET_ALL})\t{item['name']}")
    print("-" * 30)
    while True:
        game_number = input("Select new game: ").strip()
        try:
            game_number = int(game_number)
        except Exception:
            print(f"{Fore.RED}Please insert a number.{Style.RESET_ALL}")
            continue
        if game_number in range(len(GAME_TYPES)):
            valid = False
            while True:
                validity = input(
                    f"Chosen game: {Fore.BLUE}{GAME_TYPES[game_number]['name']}{Style.RESET_ALL}. Is this correct? (Y/n): "
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
            print(f"{Fore.RED}Please insert a valid number.{Style.RESET_ALL}")
            continue
    return GAME_TYPES[game_number]


def choose_players(game: Game, current_game_type: dict) -> Union[None, object]:
    while True:
        players = input(
            f"""
({Fore.BLUE}1{Style.RESET_ALL})\t{game.players[0].name}
({Fore.BLUE}2{Style.RESET_ALL})\t{game.players[1].name}
({Fore.BLUE}3{Style.RESET_ALL})\t{game.players[2].name}
({Fore.BLUE}4{Style.RESET_ALL})\t{game.players[3].name}\n
({Fore.BLUE}p{Style.RESET_ALL})\tPrevious screen\n
Who is playing {Fore.BLUE}{current_game_type['name']}{Style.RESET_ALL}? If more players, please separate with a space: """
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
            print(f"{Fore.RED}An exception occurred: {e}{Style.RESET_ALL}")
    return current_game
