from enum import Enum, auto

class ActionType(Enum):

    INITIALIZATION = 1
    SHOOT = auto()
    USE_ITEM = auto()
    TARGET_PLAYER = auto()
    LOADING_DOUBLE_DAMAGE_SHELL = auto()
    SWITCHING_SHELL = auto()
    EJECTING_SHELL = auto()
    PEEK_LOADED_SHELL = auto()
    REMOVING_ITEM_FROM_INVENTORY = auto()
    HAND_CUFF_PLAYER = auto()
    EATING_BANANA = auto()


    