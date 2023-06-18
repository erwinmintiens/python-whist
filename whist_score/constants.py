import os
import sys
from distutils.sysconfig import get_python_lib

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
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
CONFIG_FOLDER = os.path.join(ROOT_FOLDER, "config/")
if sys.platform.startswith("win"):
    SAVE_FOLDER = os.path.join(get_python_lib(), ".whist_score", "saves")
else:
    SAVE_FOLDER = os.path.join(os.path.expanduser("~"), ".whist_score", "saves")
SOLO_POINT_SYSTEM_FILE_NAME = "solo_point_system.json"
ABONDANCE_POINT_SYSTEM_FILE_NAME = "abondance_point_system.json"
MISERIE_POINT_SYSTEM_FILE_NAME = "miserie_point_system.json"
TROEL_POINT_SYSTEM_FILE_NAME = "troel_point_system.json"
VRAGEN_EN_MEEGAAN_POINT_SYSTEM_FILE_NAME = "vragen_en_meegaan_point_system.json"
GAME_TYPES_FILE_NAME = "game_types.json"
TOTAL_HEADER_LENGTH = 30
BANNER_PADDING_LENGTH = 55
GAME_SETTINGS = [{"name": "display_scoresheet_on_menu", "value": True}]
POINT_SYSTEM_SETTINGS = [
    {
        "name": "Point System",
        "options": [
            SOLO,
            VRAGEN_EN_MEEGAAN,
            TROEL,
            ABONDANCE,
            KLEINE_MISERIE,
            PICCOLO,
            GROTE_MISERIE,
            GROTE_MISERIE_OP_TAFEL,
            KLEINE_SOLO_SLIM,
            GROTE_SOLO_SLIM,
        ],
    }
]
ROOT_SETTINGS = [GAME_SETTINGS]
