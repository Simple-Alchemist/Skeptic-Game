from typing import Protocol, runtime_checkable

from ..session import Session
from ..data_classes import ActionResult
from ...core import ItemType


@runtime_checkable
class CommandInterface(Protocol):

    def execute(self, session: Session) -> ActionResult:
        ...


@runtime_checkable
class ItemCommandInterface(CommandInterface, Protocol):

    _item_type: ItemType 

    @property 
    def item_type(self) -> ItemType:
        ...

@runtime_checkable
class TargetPlayerCommandInterface(CommandInterface, Protocol):

    _target_player_id: int

    @property
    def target_player_id(self) -> int:
        ...
