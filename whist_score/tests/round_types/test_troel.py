import pytest

from whist_score.constants import TROEL_POINT_SYSTEM_FILE_NAME
from whist_score.models.RoundTypes import Troel
from whist_score.tests.utils import (
    check_scores,
    generate_players,
    get_point_system_config,
)


@pytest.mark.parametrize(
    "trump_changed",
    [
        False,
        True,
    ],
)
def test_assign_points(trump_changed):
    for number_of_tricks_achieved in range(0, 14):
        player1, player2, player3, player4 = generate_players()
        point_system = get_point_system_config(TROEL_POINT_SYSTEM_FILE_NAME)
        expected_points = [
            point_system.get("other_players", {})
            .get("trump_changed" if trump_changed else "trump_kept", {})
            .get(str(number_of_tricks_achieved)),
            point_system.get("other_players", {})
            .get("trump_changed" if trump_changed else "trump_kept", {})
            .get(str(number_of_tricks_achieved)),
            point_system.get("player", {})
            .get("trump_changed" if trump_changed else "trump_kept", {})
            .get(str(number_of_tricks_achieved)),
            point_system.get("player", {})
            .get("trump_changed" if trump_changed else "trump_kept", {})
            .get(str(number_of_tricks_achieved)),
        ]
        round_type = Troel(
            number_of_tricks=9 if trump_changed else 8,
            playing_players=[player3, player4],
            other_players=[player1, player2],
            trump_changed=trump_changed,
        )
        round_type.assign_points(tricks_achieved=number_of_tricks_achieved)
        check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize("number_of_tricks", [6, 7, 10, 11])
def test_wrong_number_of_tricks(number_of_tricks):
    player1, player2, player3, player4 = generate_players()
    with pytest.raises(ValueError):
        Troel(
            number_of_tricks=number_of_tricks,
            playing_players=[player2, player3],
            other_players=[player1, player4],
        )
