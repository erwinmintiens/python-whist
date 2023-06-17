import sys
import unittest
from io import StringIO

from whist_score.constants import TOTAL_HEADER_LENGTH
from whist_score.models.Message import Message, bcolors


class MessageTest(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        self.message = Message()

    def test_message(self):
        output = "Test message!"
        self.message.message(output)

        sys.stdout = sys.__stdout__

        printed_text = self.captured_output.getvalue().strip()
        self.assertEqual(printed_text, output)

    def test_error_message(self):
        output = "Test error message."
        expected_output = f"{bcolors.FAIL}{output}{bcolors.ENDC}"
        self.message.error(output)
        sys.stdout = sys.__stdout__
        printed_text = self.captured_output.getvalue().strip()
        self.assertEqual(printed_text, expected_output)

    def test_options(self):
        option = "X"
        output_message = "Test options message."
        expected_output = f"({bcolors.OKBLUE}{option}{bcolors.ENDC}){output_message}"
        self.message.options(
            option=option, message=output_message, remove_first_letter_of_message=False
        )
        sys.stdout = sys.__stdout__
        printed_text = self.captured_output.getvalue().strip()
        self.assertEqual(printed_text, expected_output)

    def test_options_with_removal_of_first_letter_of_message(self):
        option = "X"
        output_message = "Test options message."
        expected_output = (
            f"({bcolors.OKBLUE}{option}{bcolors.ENDC}){output_message[1:]}"
        )
        self.message.options(option=option, message=output_message)
        sys.stdout = sys.__stdout__
        printed_text = self.captured_output.getvalue().strip()
        self.assertEqual(printed_text, expected_output)

    def test_success(self):
        output = "Test success message!"
        expected_output = f"{bcolors.OKGREEN}{output}{bcolors.ENDC}"
        self.message.success(output)
        sys.stdout = sys.__stdout__
        printed_text = self.captured_output.getvalue().strip()
        self.assertEqual(printed_text, expected_output)

    def test_header(self):
        header_values = ["Menu", "Main menu", "Other test title"]
        for header_value in header_values:
            self.captured_output = StringIO()
            sys.stdout = self.captured_output
            self.message = Message()
            expected_output = f"{'-' * ((TOTAL_HEADER_LENGTH - len(header_value))// 2 - 1)} {header_value} {'-' * ((TOTAL_HEADER_LENGTH - len(header_value)) // 2 - 1)}"
            self.message.header(header_value)
            sys.stdout = sys.__stdout__
            printed_text = self.captured_output.getvalue().strip()
            self.assertEqual(printed_text, expected_output)
