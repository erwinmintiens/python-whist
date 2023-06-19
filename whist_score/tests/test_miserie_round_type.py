import pytest

from whist_score.constants import MISERIE_POINT_SYSTEM_FILE_NAME
from whist_score.models.RoundTypes import (
    GroteMiserie,
    GroteMiserieOpTafel,
    KleineMiserie,
    Piccolo,
)
from whist_score.tests.utils import (
    check_scores,
    generate_players,
    get_point_system_config,
)


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
    points_system = get_point_system_config(MISERIE_POINT_SYSTEM_FILE_NAME)
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
    points_system = get_point_system_config(MISERIE_POINT_SYSTEM_FILE_NAME)
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
    points_system = get_point_system_config(MISERIE_POINT_SYSTEM_FILE_NAME)
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
    points_system = get_point_system_config(MISERIE_POINT_SYSTEM_FILE_NAME)
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
    points_system = get_point_system_config(MISERIE_POINT_SYSTEM_FILE_NAME)
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
    points_system = get_point_system_config(MISERIE_POINT_SYSTEM_FILE_NAME)
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
    points_system = get_point_system_config(MISERIE_POINT_SYSTEM_FILE_NAME)
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
    points_system = get_point_system_config(MISERIE_POINT_SYSTEM_FILE_NAME)
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
