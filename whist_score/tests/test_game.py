import sys
import unittest
from io import StringIO
from unittest import mock

from whist_score.models.Game import Game
from whist_score.models.Player import Player


class MessageTest(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        self.game = Game(
            players=[
                Player("Player1"),
                Player("Player2"),
                Player("Player3"),
                Player("Player4"),
            ]
        )

    def test_remove_record_from_scoresheet(self):
        input_scoresheet = [[0, 10, 20, 30], [45, 35, 25, 15]]
        expected_value = input_scoresheet[:-1]
        self.game.scoresheet = input_scoresheet
        self.game.remove_record_from_scoresheet()
        self.assertEqual(self.game.scoresheet, expected_value)

    @mock.patch("whist_score.models.Message.Message.error")
    @mock.patch("whist_score.models.Message.Message.input")
    def test_remove_record_from_scoresheet_no_records(self, mock_input, mock_error):
        mock_input.return_value = "y"
        input_scoresheet = []
        self.game.scoresheet = input_scoresheet
        self.game.remove_record()
        mock_error.assert_called_once()

    @mock.patch("whist_score.models.Message.Message.input")
    def test_get_record_to_modify(self, mock_input):
        self.game.scoresheet = [[100, 110, 120, 130], [45, 46, 47, 48]]
        mock_input.side_effect = ["1", "2"]
        for i in range(1, 3):
            record = self.game.get_record_to_modify()
            self.assertEqual(record, i)

    @mock.patch("whist_score.models.Message.Message.error")
    @mock.patch("whist_score.models.Message.Message.input")
    def test_get_record_to_modify_record_not_exists(self, mock_input, mock_error):
        self.game.scoresheet = [[100, 110, 120, 130], [45, 46, 47, 48]]
        mock_input.side_effect = ["3", "q"]
        self.game.get_record_to_modify()
        mock_error.assert_called_once()

    @mock.patch("whist_score.models.Message.Message.input")
    def test_modify_record(self, mock_input):
        mock_input.side_effect = ["12 x x x", "x x x x", "0 0 0 0"]
        input_scoresheet = [
            [100, 110, 120, 130],
            [45, 46, 47, 48],
            [1000, 1000, 1000, 1000],
        ]
        self.game.scoresheet = input_scoresheet
        records_to_modify = [1, 2, 3]
        for record in records_to_modify:
            self.game.modify_record(record)

        self.assertEqual(
            self.game.scoresheet, [[12, 110, 120, 130], [45, 46, 47, 48], [0, 0, 0, 0]]
        )

    @mock.patch("whist_score.models.Message.Message.error")
    @mock.patch("whist_score.models.Message.Message.input")
    def test_modify_record_error(self, mock_input, mock_error):
        mock_input.side_effect = ["12 x x x x", "x", "x x x x", "0 x x x"]
        input_scoresheet = [
            [100, 110, 120, 130],
            [45, 46, 47, 48],
            [1000, 1000, 1000, 1000],
        ]
        self.game.scoresheet = input_scoresheet
        self.game.modify_record(1)
        self.assertEqual(mock_error.call_count, 2)
