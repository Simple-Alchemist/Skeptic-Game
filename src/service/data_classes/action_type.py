from enum import Enum, auto

class ActionType(Enum):

    SHOOT = auto()
    USE_ITEM = auto()
    RANDOM_CMD = auto()
    TARGET_PLAYER = auto()
    REMOVING_ITEM_FROM_INVENTORY = auto()
    ITEM_DISTRIBUTION = auto()
    LOAD_SHELL = auto()
    HAND_CUFF_PLAYER = auto()
    START_ROUND = auto()
    ADD_PLAYER = auto()


    