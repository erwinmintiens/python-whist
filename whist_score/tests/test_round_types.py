from whist_score.models.RoundTypes import (
    Solo,
    KleineMiserie,
    GroteMiserie,
    GroteMiserieOpTafel,
    VragenEnMeegaan,
    Troel,
    Piccolo,
    Abondance,
)
import pytest
from whist_score.models.Player import Player
from whist_score.utils import read_json
from whist_score.constants import CONFIG_FOLDER, MISERIE_POINT_SYSTEM_FILE_NAME


def generate_players():
    return Player("Player1"), Player("Player2"), Player("Player3"), Player("Player4")


def check_scores(players: list, scores: list):
    for index, player in enumerate(players):
        assert player.score == scores[index]


def get_point_system_config():
    return read_json(f"{CONFIG_FOLDER}{MISERIE_POINT_SYSTEM_FILE_NAME}")


@pytest.mark.parametrize(
    "players",
    [
        [Player("Player1")],
        [Player("Player1"), Player("Player2"), Player("Player3")],
        [Player("Player1"), Player("Player2"), Player("Player3"), Player("Player4")],
    ],
)
def test_vragen_en_meegaan_wrong_number_of_players(players):
    with pytest.raises(ValueError):
        VragenEnMeegaan(number_of_tricks=9, playing_players=players)


@pytest.mark.parametrize(
    "players",
    [
        [Player("Player1"), Player("Player2")],
        [Player("Player1"), Player("Player2"), Player("Player3")],
        [Player("Player1"), Player("Player2"), Player("Player3"), Player("Player4")],
    ],
)
def test_solo_wrong_number_of_players(players):
    with pytest.raises(ValueError):
        Solo(number_of_tricks=6, playing_players=players)


@pytest.mark.parametrize(
    "players",
    [
        [Player("Player1"), Player("Player2")],
        [Player("Player1"), Player("Player2"), Player("Player3")],
        [Player("Player1"), Player("Player2"), Player("Player3"), Player("Player4")],
    ],
)
def test_abondance_wrong_number_of_players(players):
    with pytest.raises(ValueError):
        Abondance(number_of_tricks=9, playing_players=players)


@pytest.mark.parametrize(
    "players",
    [
        [Player("Player1")],
        [Player("Player1"), Player("Player2"), Player("Player3")],
        [Player("Player1"), Player("Player2"), Player("Player3"), Player("Player4")],
    ],
)
def test_troel_wrong_number_of_players(players):
    with pytest.raises(ValueError):
        Troel(number_of_tricks=9, playing_players=players)


def test_kleine_miserie_assign_points_1_player_failed():
    player1, player2, player3, player4 = generate_players()
    player1.succeeded_round = False
    round_type = KleineMiserie(
        playing_players=[player1],
        other_players=[player2, player3, player4],
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], [-18, 12, 12, 12])


@pytest.mark.parametrize(
    "game_type,game_class",
    [
        ("kleine_miserie", KleineMiserie),
        ("grote_miserie", GroteMiserie),
        ("grote_miserie_op_tafel", GroteMiserieOpTafel),
        ("piccolo", Piccolo),
    ],
)
def test_miserie_types_assign_points_1_player_succeeded(game_type, game_class):
    player1, player2, player3, player4 = generate_players()
    player4.succeeded_round = True
    points_system = get_point_system_config()
    expected_points = [0, 0, 0, points_system[game_type]["punten_geslaagd"]]
    round_type = game_class(
        playing_players=[player4], other_players=[player1, player2, player3]
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize(
    "game_type,game_class",
    [
        ("kleine_miserie", KleineMiserie),
        ("grote_miserie", GroteMiserie),
        ("grote_miserie_op_tafel", GroteMiserieOpTafel),
        ("piccolo", Piccolo),
    ],
)
def test_miserie_types_assign_points_1_player_failed(game_type, game_class):
    player1, player2, player3, player4 = generate_players()
    player3.succeeded_round = False
    points_system = get_point_system_config()
    expected_points = [
        points_system[game_type]["punten_anderen_niet_geslaagd"]["1"],
        points_system[game_type]["punten_anderen_niet_geslaagd"]["1"],
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_anderen_niet_geslaagd"]["1"],
    ]
    round_type = game_class(
        playing_players=[player3], other_players=[player1, player2, player4]
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize(
    "game_type,game_class",
    [
        ("kleine_miserie", KleineMiserie),
        ("grote_miserie", GroteMiserie),
        ("grote_miserie_op_tafel", GroteMiserieOpTafel),
        ("piccolo", Piccolo),
    ],
)
def test_miserie_types_assign_points_1_player_succeeded_1_failed(game_type, game_class):
    player1, player2, player3, player4 = generate_players()
    player1.succeeded_round = True
    player2.succeeded_round = False
    points_system = get_point_system_config()
    expected_points = [
        points_system[game_type]["punten_geslaagd"],
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_anderen_niet_geslaagd"]["1"],
        points_system[game_type]["punten_anderen_niet_geslaagd"]["1"],
    ]
    round_type = game_class(
        playing_players=[player1, player2], other_players=[player3, player4]
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize(
    "game_type,game_class",
    [
        ("kleine_miserie", KleineMiserie),
        ("grote_miserie", GroteMiserie),
        ("grote_miserie_op_tafel", GroteMiserieOpTafel),
        ("piccolo", Piccolo),
    ],
)
def test_miserie_types_assign_points_2_players_succeeded(game_type, game_class):
    player1, player2, player3, player4 = generate_players()
    player1.succeeded_round = True
    player2.succeeded_round = True
    points_system = get_point_system_config()
    expected_points = [
        points_system[game_type]["punten_geslaagd"],
        points_system[game_type]["punten_geslaagd"],
        0,
        0,
    ]
    round_type = game_class(
        playing_players=[player1, player2], other_players=[player3, player4]
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize(
    "game_type,game_class",
    [
        ("kleine_miserie", KleineMiserie),
        ("grote_miserie", GroteMiserie),
        ("grote_miserie_op_tafel", GroteMiserieOpTafel),
        ("piccolo", Piccolo),
    ],
)
def test_miserie_types_assign_points_2_players_failed(game_type, game_class):
    player1, player2, player3, player4 = generate_players()
    player1.succeeded_round = False
    player2.succeeded_round = False
    points_system = get_point_system_config()
    expected_points = [
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_anderen_niet_geslaagd"]["2"],
        points_system[game_type]["punten_anderen_niet_geslaagd"]["2"],
    ]
    round_type = game_class(
        playing_players=[player1, player2], other_players=[player3, player4]
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize(
    "game_type,game_class",
    [
        ("kleine_miserie", KleineMiserie),
        ("grote_miserie", GroteMiserie),
        ("grote_miserie_op_tafel", GroteMiserieOpTafel),
        ("piccolo", Piccolo),
    ],
)
def test_miserie_types_assign_points_2_players_failed_1_succeeded(
    game_type, game_class
):
    player1, player2, player3, player4 = generate_players()
    player1.succeeded_round = False
    player2.succeeded_round = False
    player4.succeeded_round = True
    points_system = get_point_system_config()
    expected_points = [
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_anderen_niet_geslaagd"]["2"],
        points_system[game_type]["punten_geslaagd"],
    ]
    round_type = game_class(
        playing_players=[player1, player2, player4], other_players=[player3]
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize(
    "game_type,game_class",
    [
        ("kleine_miserie", KleineMiserie),
        ("grote_miserie", GroteMiserie),
        ("grote_miserie_op_tafel", GroteMiserieOpTafel),
        ("piccolo", Piccolo),
    ],
)
def test_miserie_types_assign_points_3_players_failed(game_type, game_class):
    player1, player2, player3, player4 = generate_players()
    player1.succeeded_round = False
    player2.succeeded_round = False
    player4.succeeded_round = False
    points_system = get_point_system_config()
    expected_points = [
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_anderen_niet_geslaagd"]["3"],
        points_system[game_type]["punten_niet_geslaagd"],
    ]
    round_type = game_class(
        playing_players=[player1, player2, player4], other_players=[player3]
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize(
    "game_type,game_class",
    [
        ("kleine_miserie", KleineMiserie),
        ("grote_miserie", GroteMiserie),
        ("grote_miserie_op_tafel", GroteMiserieOpTafel),
        ("piccolo", Piccolo),
    ],
)
def test_miserie_types_assign_points_3_players_failed_1_succeeded(
    game_type, game_class
):
    player1, player2, player3, player4 = generate_players()
    player1.succeeded_round = False
    player2.succeeded_round = False
    player3.succeeded_round = True
    player4.succeeded_round = False
    points_system = get_point_system_config()
    expected_points = [
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_niet_geslaagd"],
        points_system[game_type]["punten_geslaagd"],
        points_system[game_type]["punten_niet_geslaagd"],
    ]
    round_type = game_class(
        playing_players=[player1, player2, player3, player4], other_players=[]
    )
    round_type.assign_points()
    check_scores([player1, player2, player3, player4], expected_points)
