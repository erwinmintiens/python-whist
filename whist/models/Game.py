from typing import Union
import json
import os

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
    TROEL_POINT_SYSTEM,
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

    def save(self):
        payload = {
            "current_round": self.current_round,
            "scoresheet": self.scoresheet,
            "players": [player.name for player in self.players],
        }
        while True:
            answer = input("Give a name for the file: ").strip()
            try:
                with open(f"{SAVE_FOLDER}{answer}.json", "w") as f:
                    json.dump(payload, f, indent=2)
                break
            except Exception as e:
                print(e.__repr__())
                continue
        print(f"Successfully saved to {SAVE_FOLDER}{answer}.json")


class BaseRoundClass:
    def __init__(self, playing_players: list = [], other_players: list = []):
        self.playing_players = playing_players
        self.other_players = other_players

    def complete(self):
        for player in self.playing_players:
            player.has_succeeded = False
        while True:
            succeeded = input("Did the player(s) succeed? (Y/n): ").strip()
            if succeeded in ("Y", "y", ""):
                for player in self.playing_players:
                    player.has_succeeded = True
                break
            elif succeeded in ("N", "n"):
                pass
            else:
                continue
            answer = input("Did some players succeed? (Y/n): ")
            if answer in ("Y", "y", ""):
                self.choose_succeeded_players()
                break
            elif answer in ("N", "n"):
                break
            else:
                continue

    def choose_succeeded_players(self):
        while True:
            for index, player in enumerate(self.playing_players):
                print(f"({index})\t{player.name}")
            answer = input(
                "Please choose the players that succeeded. Separate with a space if needed (q to quit to previous question): "
            )
            try:
                answer = answer.split()
                if answer == ["q"] or answer == ["Q"]:
                    break
                for item in answer:
                    if int(item) not in range(len(self.playing_players)):
                        continue
                break
            except Exception:
                continue
        if answer != ["q"] and answer != ["Q"]:
            for item in answer:
                self.playing_players[int(item)].has_succeeded = True

    def assign_points(self, tricks_achieved: int, point_system: dict) -> None:
        for player in self.playing_players:
            player.add_to_score(
                point_system[str(self.number_of_tricks)]["player"][str(tricks_achieved)]
            )
        for player in self.other_players:
            player.add_to_score(
                point_system[str(self.number_of_tricks)]["other_players"][
                    str(tricks_achieved)
                ]
            )


class Abondance(BaseRoundClass):
    def __init__(
        self,
        number_of_tricks: int,
        playing_players: list = [],
        other_players: list = [],
    ) -> None:
        self.number_of_tricks = number_of_tricks
        if len(playing_players) != 1:
            raise ValueError("There can only be 1 player in a game of Abondance.")
        super().__init__(playing_players=playing_players, other_players=other_players)

    def assign_points(self, tricks_achieved: int):
        super().assign_points(
            tricks_achieved=tricks_achieved, point_system=ABONDANCE_POINT_SYSTEM
        )


class VragenEnMeegaan(BaseRoundClass):
    def __init__(
        self,
        number_of_tricks: int,
        playing_players: list = [],
        other_players: list = [],
    ) -> None:
        self.number_of_tricks = number_of_tricks
        if len(playing_players) != 2:
            raise ValueError(
                "There can only be 2 players in a game of vragen en meegaan."
            )
        super().__init__(playing_players=playing_players, other_players=other_players)

    def assign_points(self, tricks_achieved: int) -> None:
        super().assign_points(
            tricks_achieved=tricks_achieved, point_system=VRAGEN_EN_MEEGAAN_POINT_SYSTEM
        )


class Troel(VragenEnMeegaan):
    def __init__(
        self,
        number_of_tricks: int,
        playing_players: list = [],
        other_players: list = [],
    ) -> None:
        super().__init__(
            number_of_tricks=number_of_tricks,
            playing_players=playing_players,
            other_players=other_players,
        )

    def assign_points(
        self, tricks_achieved: int, point_system: dict = TROEL_POINT_SYSTEM
    ) -> None:
        for player in self.playing_players:
            player.add_to_score(point_system["player"][str(tricks_achieved)])
        for player in self.other_players:
            player.add_to_score(point_system["other_players"][str(tricks_achieved)])


class Solo(BaseRoundClass):
    def __init__(
        self,
        number_of_tricks: int,
        playing_players: list = [],
        other_players: list = [],
    ) -> None:
        self.number_of_tricks = number_of_tricks
        if len(playing_players) != 1:
            raise ValueError("There can only be 1 player in a game of Solo.")
        super().__init__(playing_players=playing_players, other_players=other_players)

    def assign_points(self, tricks_achieved: int) -> None:
        super().assign_points(
            tricks_achieved=tricks_achieved, point_system=SOLO_POINT_SYSTEM
        )


class BaseMiserieClass(BaseRoundClass):
    def __init__(self, playing_players: list = [], other_players: list = []) -> None:
        self.number_of_tricks = 0
        super().__init__(playing_players=playing_players, other_players=other_players)

    def assign_points(self, point_system: str) -> None:
        number_of_failed_players = [
            player.has_succeeded for player in self.playing_players
        ].count(False)
        for player in self.playing_players:
            player.add_to_score(
                MISERIE_POINT_SYSTEM[point_system]["punten_geslaagd"]
            ) if player.has_succeeded else player.add_to_score(
                MISERIE_POINT_SYSTEM[point_system]["punten_niet_geslaagd"]
            )
        if number_of_failed_players == 1:
            for player in self.other_players:
                player.add_to_score(
                    MISERIE_POINT_SYSTEM[point_system]["punten_anderen_niet_geslaagd"][
                        "1"
                    ]
                )
        elif number_of_failed_players == 2:
            for player in self.other_players:
                player.add_to_score(
                    MISERIE_POINT_SYSTEM[point_system]["punten_anderen_niet_geslaagd"][
                        "2"
                    ]
                )
        elif number_of_failed_players == 3:
            for player in self.other_players:
                player.add_to_score(
                    MISERIE_POINT_SYSTEM[point_system]["punten_anderen_niet_geslaagd"][
                        "3"
                    ]
                )


class KleineMiserie(BaseMiserieClass):
    def __init__(self, playing_players: list = [], other_players: list = []) -> None:
        super().__init__(playing_players=playing_players, other_players=other_players)

    def assign_points(self, point_system="kleine_miserie"):
        super().assign_points(
            point_system=point_system,
        )


class Piccolo(BaseMiserieClass):
    def __init__(self, playing_players: list = [], other_players: list = []) -> None:
        super().__init__(playing_players=playing_players, other_players=other_players)

    def assign_points(self, point_system="piccolo"):
        super().assign_points(
            point_system=point_system,
        )


class GroteMiserie(BaseMiserieClass):
    def __init__(self, playing_players: list = [], other_players: list = []) -> None:
        super().__init__(playing_players=playing_players, other_players=other_players)

    def assign_points(self, point_system="grote_miserie"):
        super().assign_points(
            point_system=point_system,
        )


class GroteMiserieOpTafel(BaseMiserieClass):
    def __init__(self, playing_players: list = [], other_players: list = []) -> None:
        super().__init__(playing_players=playing_players, other_players=other_players)

    def assign_points(self, point_system="grote_miserie_op_tafel"):
        super().assign_points(
            point_system=point_system,
        )
