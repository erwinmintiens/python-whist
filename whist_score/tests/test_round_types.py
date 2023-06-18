import pytest

from whist_score.models.Player import Player
from whist_score.models.RoundTypes import Abondance, Solo, Troel, VragenEnMeegaan


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
