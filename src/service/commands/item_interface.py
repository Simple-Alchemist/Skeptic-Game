from typing import Protocol, runtime_checkable
from .interface import CommandInterface

from ...core import ItemType


@runtime_checkable
class ItemCommandInterface(CommandInterface, Protocol):

    _item_type: ItemType 

    @property 
    def item_type(self) -> ItemType:
        ...


    

    