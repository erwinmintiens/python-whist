import pytest

from whist_score.constants import ABONDANCE_POINT_SYSTEM_FILE_NAME
from whist_score.models.RoundTypes import Abondance
from whist_score.tests.utils import (
    check_scores,
    generate_players,
    get_point_system_config,
)


@pytest.mark.parametrize(
    "number_of_tricks,number_of_tricks_achieved",
    [
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (9, 10),
        (9, 11),
        (9, 12),
        (9, 13),
        (10, 11),
        (10, 12),
        (10, 13),
        (11, 12),
        (11, 13),
        (12, 13),
        (9, 8),
        (9, 7),
        (10, 9),
        (10, 8),
        (11, 10),
        (11, 9),
        (12, 11),
        (12, 10),
        (13, 12),
        (13, 11),
    ],
)
def test_abondance_assign_points(number_of_tricks, number_of_tricks_achieved):
    player1, player2, player3, player4 = generate_players()
    point_system = get_point_system_config(ABONDANCE_POINT_SYSTEM_FILE_NAME)
    expected_points = [
        point_system.get(str(number_of_tricks), {})
        .get("player", {})
        .get(str(number_of_tricks_achieved)),
        point_system.get(str(number_of_tricks), {})
        .get("other_players", {})
        .get(str(number_of_tricks_achieved)),
        point_system.get(str(number_of_tricks), {})
        .get("other_players", {})
        .get(str(number_of_tricks_achieved)),
        point_system.get(str(number_of_tricks), {})
        .get("other_players", {})
        .get(str(number_of_tricks_achieved)),
    ]
    round_type = Abondance(
        number_of_tricks=number_of_tricks,
        playing_players=[player1],
        other_players=[player2, player3, player4],
    )
    round_type.assign_points(tricks_achieved=number_of_tricks_achieved)
    check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize("number_of_tricks", [7, 8, 14])
def test_abondance_wrong_number_of_tricks(number_of_tricks):
    player1, player2, player3, player4 = generate_players()
    with pytest.raises(ValueError):
        Abondance(
            number_of_tricks=number_of_tricks,
            playing_players=[player2],
            other_players=[player1, player3, player4],
        )
