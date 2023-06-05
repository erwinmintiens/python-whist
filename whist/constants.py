MISERIE = "Miserie"
KLEINE_MISERIE = f"Kleine {MISERIE}"
GROTE_MISERIE = f"Grote {MISERIE}"
GROTE_MISERIE_OP_TAFEL = f"{GROTE_MISERIE} op tafel"
SOLO_SLIM = "Solo Slim"
KLEINE_SOLO_SLIM = f"Kleine {SOLO_SLIM}"
GROTE_SOLO_SLIM = f"Grote {SOLO_SLIM}"
VRAGEN_EN_MEEGAAN = "Vragen en Meegaan"
SOLO = "Solo"
TROEL = "Troel"
PICCOLO = "Piccolo"
ABONDANCE = "Abondance"

GAME_TYPES = [
    {"id": 1, "name": f"{VRAGEN_EN_MEEGAAN} 8", "number_of_tricks": 8},
    {"id": 2, "name": f"{VRAGEN_EN_MEEGAAN} 9", "number_of_tricks": 9},
    {"id": 3, "name": f"{VRAGEN_EN_MEEGAAN} 10", "number_of_tricks": 10},
    {"id": 4, "name": f"{VRAGEN_EN_MEEGAAN} 11", "number_of_tricks": 11},
    {"id": 5, "name": f"{VRAGEN_EN_MEEGAAN} 12", "number_of_tricks": 12},
    {"id": 6, "name": f"{VRAGEN_EN_MEEGAAN} 13", "number_of_tricks": 13},
    {"id": 7, "name": f"{SOLO} 6", "number_of_tricks": 6},
    {"id": 8, "name": f"{SOLO} 7", "number_of_tricks": 7},
    {"id": 9, "name": f"{SOLO} 8", "number_of_tricks": 8},
    {"id": 10, "name": TROEL, "number_of_tricks": 9},
    {"id": 11, "name": f"{ABONDANCE} 9", "number_of_tricks": 9},
    {"id": 12, "name": f"{ABONDANCE} 10", "number_of_tricks": 10},
    {"id": 13, "name": f"{ABONDANCE} 11", "number_of_tricks": 11},
    {"id": 14, "name": KLEINE_MISERIE, "number_of_tricks": 0},
    {"id": 15, "name": PICCOLO, "number_of_tricks": 1},
    {"id": 16, "name": GROTE_MISERIE, "number_of_tricks": 0},
    {"id": 17, "name": GROTE_MISERIE_OP_TAFEL, "number_of_tricks": 0},
    {"id": 18, "name": KLEINE_SOLO_SLIM, "number_of_tricks": 12},
    {"id": 19, "name": GROTE_SOLO_SLIM, "number_of_tricks": 13},
]


MISERIE_POINT_SYSTEM = {
    "kleine_miserie": {
        "punten_geslaagd": 18,
        "punten_niet_geslaagd": -18,
        "punten_anderen_niet_geslaagd": {"1": 12, "2": 24, "3": 36},
    },
    "piccolo": {
        "punten_geslaagd": 27,
        "punten_niet_geslaagd": -27,
        "punten_anderen_niet_geslaagd": {"1": 18, "2": 36, "3": 54},
    },
    "grote_miserie": {
        "punten_geslaagd": 36,
        "punten_niet_geslaagd": -36,
        "punten_anderen_niet_geslaagd": {"1": 24, "2": 48, "3": 72},
    },
    "grote_miserie_op_tafel": {
        "punten_geslaagd": 72,
        "punten_niet_geslaagd": -72,
        "punten_anderen_niet_geslaagd": {"1": 48, "2": 96, "3": 144},
    },
}

TROEL_POINT_SYSTEM = {
    "player": {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 15,
        "10": 15,
        "11": 15,
        "12": 15,
        "13": 15,
    },
    "other_players": {
        "1": 15,
        "2": 15,
        "3": 15,
        "4": 15,
        "5": 15,
        "6": 15,
        "7": 15,
        "8": 15,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0,
        "13": 0,
    },
}

SOLO_POINT_SYSTEM = {
    "6": {
        "player": {
            "1": -27,
            "2": -24,
            "3": -21,
            "4": -18,
            "5": -15,
            "6": 12,
            "7": 15,
            "8": 18,
            "9": 18,
            "10": 18,
            "11": 18,
            "12": 18,
            "13": 18,
        },
        "other_players": {
            "1": 18,
            "2": 16,
            "3": 14,
            "4": 12,
            "5": 10,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "7": {
        "player": {
            "1": -33,
            "2": -30,
            "3": -27,
            "4": -24,
            "5": -21,
            "6": -18,
            "7": 15,
            "8": 18,
            "9": 18,
            "10": 18,
            "11": 18,
            "12": 18,
            "13": 18,
        },
        "other_players": {
            "1": 22,
            "2": 20,
            "3": 18,
            "4": 16,
            "5": 14,
            "6": 12,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "8": {
        "player": {
            "1": -42,
            "2": -39,
            "3": -36,
            "4": -33,
            "5": -30,
            "6": -27,
            "7": -24,
            "8": 21,
            "9": 21,
            "10": 21,
            "11": 21,
            "12": 21,
            "13": 21,
        },
        "other_players": {
            "1": 28,
            "2": 26,
            "3": 24,
            "4": 22,
            "5": 20,
            "6": 18,
            "7": 16,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
}


VRAGEN_EN_MEEGAAN_POINT_SYSTEM = {
    "8": {
        "player": {
            "1": -28,
            "2": -25,
            "3": -22,
            "4": -19,
            "5": -16,
            "6": -13,
            "7": -10,
            "8": 7,
            "9": 10,
            "10": 13,
            "11": 16,
            "12": 19,
            "13": 30,
        },
        "other_players": {
            "1": 28,
            "2": 25,
            "3": 22,
            "4": 19,
            "5": 16,
            "6": 13,
            "7": 10,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "9": {
        "player": {
            "1": -34,
            "2": -31,
            "3": -28,
            "4": -25,
            "5": -22,
            "6": -19,
            "7": -16,
            "8": -13,
            "9": 10,
            "10": 13,
            "11": 16,
            "12": 19,
            "13": 30,
        },
        "other_players": {
            "1": 34,
            "2": 31,
            "3": 28,
            "4": 25,
            "5": 22,
            "6": 19,
            "7": 16,
            "8": 13,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "10": {
        "player": {
            "1": -40,
            "2": -37,
            "3": -34,
            "4": -31,
            "5": -28,
            "6": -25,
            "7": -22,
            "8": -19,
            "9": -16,
            "10": 13,
            "11": 16,
            "12": 19,
            "13": 30,
        },
        "other_players": {
            "1": 40,
            "2": 37,
            "3": 34,
            "4": 31,
            "5": 28,
            "6": 25,
            "7": 22,
            "8": 19,
            "9": 16,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "11": {
        "player": {
            "1": -46,
            "2": -43,
            "3": -40,
            "4": -37,
            "5": -34,
            "6": -31,
            "7": -28,
            "8": -25,
            "9": -22,
            "10": -19,
            "11": 16,
            "12": 19,
            "13": 30,
        },
        "other_players": {
            "1": 46,
            "2": 43,
            "3": 40,
            "4": 37,
            "5": 34,
            "6": 31,
            "7": 28,
            "8": 25,
            "9": 22,
            "10": 19,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "12": {
        "player": {
            "1": -55,
            "2": -52,
            "3": -49,
            "4": -46,
            "5": -43,
            "6": -40,
            "7": -37,
            "8": -34,
            "9": -31,
            "10": -28,
            "11": -25,
            "12": 22,
            "13": 30,
        },
        "other_players": {
            "1": 55,
            "2": 52,
            "3": 49,
            "4": 46,
            "5": 43,
            "6": 40,
            "7": 37,
            "8": 34,
            "9": 31,
            "10": 28,
            "11": 25,
            "12": 0,
            "13": 0,
        },
    },
    "13": {
        "player": {
            "1": -66,
            "2": -63,
            "3": -60,
            "4": -57,
            "5": -54,
            "6": -51,
            "7": -48,
            "8": -45,
            "9": -42,
            "10": -39,
            "11": -36,
            "12": -33,
            "13": 30,
        },
        "other_players": {
            "1": 66,
            "2": 63,
            "3": 60,
            "4": 57,
            "5": 54,
            "6": 51,
            "7": 48,
            "8": 45,
            "9": 42,
            "10": 39,
            "11": 36,
            "12": 33,
            "13": 0,
        },
    },
}

ABONDANCE_POINT_SYSTEM = {
    "9": {
        "player": {
            "1": -30,
            "2": -30,
            "3": -30,
            "4": -30,
            "5": -30,
            "6": -30,
            "7": -30,
            "8": -30,
            "9": 30,
            "10": 30,
            "11": 30,
            "12": 30,
            "13": 30,
        },
        "other_players": {
            "1": 20,
            "2": 20,
            "3": 20,
            "4": 20,
            "5": 20,
            "6": 20,
            "7": 20,
            "8": 20,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "10": {
        "player": {
            "1": -45,
            "2": -45,
            "3": -45,
            "4": -45,
            "5": -45,
            "6": -45,
            "7": -45,
            "8": -45,
            "9": -45,
            "10": 45,
            "11": 45,
            "12": 45,
            "13": 45,
        },
        "other_players": {
            "1": 30,
            "2": 30,
            "3": 30,
            "4": 30,
            "5": 30,
            "6": 30,
            "7": 30,
            "8": 30,
            "9": 30,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "11": {
        "player": {
            "1": -60,
            "2": -60,
            "3": -60,
            "4": -60,
            "5": -60,
            "6": -60,
            "7": -60,
            "8": -60,
            "9": -60,
            "10": -60,
            "11": 60,
            "12": 60,
            "13": 60,
        },
        "other_players": {
            "1": 40,
            "2": 40,
            "3": 40,
            "4": 40,
            "5": 40,
            "6": 40,
            "7": 40,
            "8": 40,
            "9": 40,
            "10": 40,
            "11": 0,
            "12": 0,
            "13": 0,
        },
    },
    "12": {
        "player": {
            "1": -100,
            "2": -100,
            "3": -100,
            "4": -100,
            "5": -100,
            "6": -100,
            "7": -100,
            "8": -100,
            "9": -100,
            "10": -100,
            "11": -100,
            "12": 100,
            "13": 100,
        },
        "other_players": {
            "1": 66,
            "2": 66,
            "3": 66,
            "4": 66,
            "5": 66,
            "6": 66,
            "7": 66,
            "8": 66,
            "9": 66,
            "10": 66,
            "11": 66,
            "12": 0,
            "13": 0,
        },
    },
    "13": {
        "player": {
            "1": -150,
            "2": -150,
            "3": -150,
            "4": -150,
            "5": -150,
            "6": -150,
            "7": -150,
            "8": -150,
            "9": -150,
            "10": -150,
            "11": -150,
            "12": -150,
            "13": 150,
        },
        "other_players": {
            "1": 100,
            "2": 100,
            "3": 100,
            "4": 100,
            "5": 100,
            "6": 100,
            "7": 100,
            "8": 100,
            "9": 100,
            "10": 100,
            "11": 100,
            "12": 100,
            "13": 0,
        },
    },
}


SAVE_FOLDER = "./results/"
