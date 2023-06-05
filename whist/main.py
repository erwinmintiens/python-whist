import click
from whist.views.games import new_game


@click.command()
@click.option("--players", help="Names of the 4 players, seperated by a semicolon (;)")
def main(players=None):
    while True:
        choice = input("(N)ew game | (L)oad game | (S)ettings\n").strip()
        if choice in ("N", "n"):
            new_game(players=players)
            break
        elif choice in ("L", "l"):
            load_game()
            break
        elif choice in ("S", "s"):
            settings()
            break
        else:
            print("Please provide a valid option.")


def load_game():
    pass


def settings():
    pass


if __name__ == "__main__":
    main()
