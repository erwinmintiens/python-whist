from colorama import Fore, Style

from whist_score.constants import (
    TOTAL_HEADER_LENGTH,
    CONFIG_FOLDER,
    GAME_TYPES_FILE_NAME,
    BANNER_PADDING_LENGTH,
)
import os
from whist_score.utils import read_json


class Message:
    def __init__(self) -> None:
        pass

    def message(self, message: str = ""):
        print(message)

    def error(self, message: str = ""):
        print(f"{Fore.RED}{message}{Style.RESET_ALL}")

    def options(self, option: str, message: str, remove_first_letter_of_message=True):
        print(
            f"({Fore.BLUE}{option}{Style.RESET_ALL}){message[1:]}"
        ) if remove_first_letter_of_message else print(
            f"({Fore.BLUE}{option}{Style.RESET_ALL}){message}"
        )

    def success(self, message: str = ""):
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")

    def banner(self, version: str, url: str):
        self.success("-" * BANNER_PADDING_LENGTH)
        self.success("          _     _     _                               ")
        self.success("__      _| |__ (_)___| |_      ___  ___ ___  _ __ ___ ")
        self.success("\ \ /\ / / '_ \| / __| __|____/ __|/ __/ _ \| '__/ _ \\")
        self.success(" \ V  V /| | | | \__ \ ||_____\__ \ (_| (_) | | |  __/")
        self.success("  \_/\_/ |_| |_|_|___/\__|    |___/\___\___/|_|  \___|")
        self.success("                                                      ")
        self.success(f"Welcome to whist-score v{version}")
        self.success(f"GitHub: {url}")
        self.success("-" * BANNER_PADDING_LENGTH)

    def header(self, value: str):
        text_length = len(value)
        padding_length = (TOTAL_HEADER_LENGTH - text_length) // 2
        padding = "-" * (padding_length - 1)
        header = f"{padding} {value} {padding}"
        self.message(header)

    def footer(self):
        self.message("-" * TOTAL_HEADER_LENGTH)

    def input(self, message: str = "> ", lower=True) -> str:
        print()
        return input(message).strip().lower() if lower else input(message).strip()

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def new_round_options(self):
        self.header("Game Types")
        game_types = read_json(f"{CONFIG_FOLDER}{GAME_TYPES_FILE_NAME}")
        for index, item in enumerate(game_types):
            self.options(
                option=index,
                message=f"\t{item['name']}",
                remove_first_letter_of_message=False,
            )
        self.footer()
