from enum import Enum, auto

class States(Enum):
    
    ROUND_MANAGER = auto()
    PLAY_STATE = auto()
    RESOLUTION_STATE = auto()
    GAME_OVER = auto()
