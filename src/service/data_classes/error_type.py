from enum import Enum, auto

class ErrorType(Enum):

    INCORRECT_COMMAND = 2001
    CURRENTLY_IN_RESOLUTION_STATE = auto()
    GAME_OVER = auto()

    UNKNOWN_PLAYER = 1001
    INSUFFICIENT_PLAYERS = auto()
    EMPTY_MAGAZINE = auto()
    ITEM_NOT_IN_INVENTORY = auto()
    HAND_CUFFING_YOURSELF = auto()
    CURRENT_PLAYER_CUFFED = auto()
    ALREADY_CUFFED = auto()
    INVALID_SHELL_STATE = auto()

    
    