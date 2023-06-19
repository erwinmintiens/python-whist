import pytest

from whist_score.constants import SOLO_POINT_SYSTEM_FILE_NAME
from whist_score.models.RoundTypes import Solo
from whist_score.tests.utils import (
    check_scores,
    generate_players,
    get_point_system_config,
)


@pytest.mark.parametrize(
    "number_of_tricks",
    [6, 7, 8],
)
def test_assign_points(number_of_tricks):
    for number_of_tricks_achieved in range(0, 14):
        player1, player2, player3, player4 = generate_players()
        point_system = get_point_system_config(SOLO_POINT_SYSTEM_FILE_NAME)
        expected_points = [
            point_system.get(str(number_of_tricks), {})
            .get("other_players", {})
            .get(str(number_of_tricks_achieved)),
            point_system.get(str(number_of_tricks), {})
            .get("player", {})
            .get(str(number_of_tricks_achieved)),
            point_system.get(str(number_of_tricks), {})
            .get("other_players", {})
            .get(str(number_of_tricks_achieved)),
            point_system.get(str(number_of_tricks), {})
            .get("other_players", {})
            .get(str(number_of_tricks_achieved)),
        ]
        round_type = Solo(
            number_of_tricks=number_of_tricks,
            playing_players=[player2],
            other_players=[player1, player3, player4],
        )
        round_type.assign_points(tricks_achieved=number_of_tricks_achieved)
        check_scores([player1, player2, player3, player4], expected_points)


@pytest.mark.parametrize("number_of_tricks", [4, 5, 9, 10])
def test_wrong_number_of_tricks(number_of_tricks):
    player1, player2, player3, player4 = generate_players()
    with pytest.raises(ValueError):
        Solo(
            number_of_tricks=number_of_tricks,
            playing_players=[player2],
            other_players=[player1, player3, player4],
        )
