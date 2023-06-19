from whist_score.constants import CONFIG_FOLDER
from whist_score.models.Player import Player
from whist_score.utils import read_json


def generate_players():
    return Player("Player1"), Player("Player2"), Player("Player3"), Player("Player4")


def check_scores(players: list, scores: list):
    for index, player in enumerate(players):
        assert player.score == scores[index]


def get_point_system_config(point_system_file_name: str):
    return read_json(f"{CONFIG_FOLDER}{point_system_file_name}")
